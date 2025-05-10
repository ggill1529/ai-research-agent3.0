# analyze.py – AI/NLP Summarization, Deduplication, Clustering

import openai
import asyncio
from core.schema import ResearchItem
from sentence_transformers import SentenceTransformer, util
from sklearn.cluster import DBSCAN
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


async def summarize_text(text: str, config) -> str:
    openai.api_key = config["openai_api_key"]
    prompt = f"Summarize the following content in 3-5 sentences focusing on AI-related insights:\n\n{text[:3000]}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("❌ Error summarizing:", e)
        return text[:1000]  # fallback


async def run_analysis_pipeline(items: list, config: dict) -> list:
    print("✍️ Summarizing items with GPT and embedding...")

    embeddings = model.encode([item.content for item in items], convert_to_tensor=True)
    summaries = await asyncio.gather(*[summarize_text(item.content, config) for item in items])

    for i, item in enumerate(items):
        item.content = summaries[i]  # Replace content with summary

    print("🔁 Deduplicating similar articles...")
    similarity_matrix = util.pytorch_cos_sim(embeddings, embeddings).numpy()
    seen = set()
    deduped_items = []

    for i, item in enumerate(items):
        if i in seen:
            continue
        dupes = np.where(similarity_matrix[i] > 0.90)[0]
        seen.update(dupes)
        deduped_items.append(item)

    print("🧠 Clustering articles by topic...")
    cluster_model = DBSCAN(eps=0.8, min_samples=2, metric="cosine")
    labels = cluster_model.fit_predict(embeddings)

    for i, item in enumerate(deduped_items):
        setattr(item, "cluster_id", labels[i])

    return deduped_items
