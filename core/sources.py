# sources.py – Data Fetching Layer

import asyncio
from core.utils.rss import fetch_rss_articles
from core.utils.youtube import fetch_youtube_videos
from core.utils.twitter import fetch_tweets
from core.utils.reddit import fetch_reddit_posts
from core.utils.arxiv import fetch_arxiv_papers


async def fetch_all_sources(config):
    tasks = []

    # Fetch from RSS/news/blogs
    for source in config.get("rss_feeds", []):
        tasks.append(fetch_rss_articles(source))

    # Fetch from YouTube
    if config.get("youtube"):
        tasks.append(fetch_youtube_videos(config["youtube"]))

    # Fetch from Twitter (snscrape)
    if config.get("twitter"):
        tasks.append(fetch_tweets(config["twitter"]))

    # Fetch from Reddit
    if config.get("reddit"):
        tasks.append(fetch_reddit_posts(config["reddit"]))

    # Fetch from arXiv
    if config.get("arxiv", True):
        tasks.append(fetch_arxiv_papers())

    # Run all fetches concurrently
    results = await asyncio.gather(*tasks)

    # Flatten nested lists
    all_items = [item for sublist in results for item in sublist]
    return all_items
