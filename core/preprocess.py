# preprocess.py – Standardize and Clean Raw Items

from core.schema import ResearchItem
from typing import List


def preprocess_items(items: List[ResearchItem]) -> List[ResearchItem]:
    print("🧹 Preprocessing content: trimming, cleaning, normalizing...")
    clean_items = []

    for item in items:
        if not item.content or len(item.content.strip()) < 40:
            continue  # Drop items with almost no content

        # Remove duplicate media URLs
        if item.media_urls:
            item.media_urls = list(set(item.media_urls))

        # Basic normalization (placeholder for more rules)
        item.title = item.title.strip()
        item.content = item.content.strip()

        clean_items.append(item)

    return clean_items
