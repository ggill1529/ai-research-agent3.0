# pipeline.py – Core Pipeline for AI Research Agent 2.0

import json
import asyncio
from datetime import datetime
from core.sources import fetch_all_sources
from core.preprocess import preprocess_items
from core.analyze import run_analysis_pipeline
from core.enrich import enrich_items_with_media
from core.report import generate_report


async def run_full_pipeline():
    print("🔄 Starting AI Research Agent 2.0 Pipeline...")

    # Load configuration and sources
    with open("config.json", "r") as f:
        config = json.load(f)

    print("📥 Fetching data from all sources...")
    raw_items = await fetch_all_sources(config)

    print(f"🧹 Preprocessing {len(raw_items)} items...")
    clean_items = preprocess_items(raw_items)

    print("🧠 Running AI/NLP analysis pipeline...")
    analyzed_items = await run_analysis_pipeline(clean_items, config)

    print("🎨 Enriching items with screenshots, media, quotes...")
    enriched_items = await enrich_items_with_media(analyzed_items, config)

    print("📝 Generating final report...")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    await generate_report(enriched_items, timestamp)

    print(f"✅ Done. Report saved as ai_research_report_{timestamp}.md/pdf/html")
