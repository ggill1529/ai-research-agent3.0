# reddit.py – Reddit Post Fetching Utility

import praw
from core.schema import ResearchItem
from datetime import datetime


def fetch_reddit_posts(config):
    print("👽 Fetching Reddit posts...")

    reddit = praw.Reddit(
        client_id=config["client_id"],
        client_secret=config["client_secret"],
        user_agent="AIResearchAgent/1.0"
    )

    subreddits = config.get("subreddits", [])
    limit = config.get("max_results", 5)
    items = []

    for sub in subreddits:
        for submission in reddit.subreddit(sub).hot(limit=limit):
            item = ResearchItem(
                title=submission.title,
                content=submission.selftext or submission.url,
                source=f"r/{sub}",
                url=submission.url,
                date=datetime.fromtimestamp(submission.created_utc),
                media_urls=[]
            )
            items.append(item)

    return items
