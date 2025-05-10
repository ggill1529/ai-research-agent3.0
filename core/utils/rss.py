# rss.py – RSS Fetching Utility

import feedparser
from datetime import datetime
from core.schema import ResearchItem


def fetch_rss_articles(source):
    print(f"🌐 Fetching RSS feed from {source['name']}...")
    feed = feedparser.parse(source['url'])
    items = []

    for entry in feed.entries[:source.get('limit', 10)]:
        pub_date = entry.get('published_parsed')
        date = datetime(*pub_date[:6]) if pub_date else datetime.now()

        item = ResearchItem(
            title=entry.get('title', 'No Title'),
            content=entry.get('summary', ''),
            source=source['name'],
            url=entry.get('link', ''),
            date=date,
            media_urls=[]
        )
        items.append(item)

    return items
