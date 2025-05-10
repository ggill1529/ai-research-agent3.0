# enrich.py – Add Media Context (Screenshots, Quotes, Thumbnails)

from core.schema import ResearchItem
from typing import List
import requests
import os


def download_image(url, save_path):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return save_path
    except:
        pass
    return None


async def enrich_items_with_media(items: List[ResearchItem], config: dict) -> List[ResearchItem]:
    print("🖼️ Enhancing items with images, thumbnails, and saved media...")
    os.makedirs("media", exist_ok=True)

    for i, item in enumerate(items):
        enriched_media = []
        for j, url in enumerate(item.media_urls or []):
            filename = f"media/{i}_{j}.jpg"
            if download_image(url, filename):
                enriched_media.append(filename)
        item.media_urls = enriched_media

    return items
