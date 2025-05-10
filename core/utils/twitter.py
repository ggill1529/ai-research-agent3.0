# twitter.py – Twitter Fetching Utility using snscrape

import snscrape.modules.twitter as sntwitter
from core.schema import ResearchItem


def fetch_tweets(config):
    print("🐦 Fetching tweets using snscrape...")
    usernames = config.get("usernames", [])
    max_tweets = config.get("max_results", 5)
    items = []

    for username in usernames:
        scraper = sntwitter.TwitterUserScraper(username)
        for i, tweet in enumerate(scraper.get_items()):
            if i >= max_tweets:
                break

            item = ResearchItem(
                title=f"Tweet from @{username}",
                content=tweet.content,
                source="Twitter",
                url=f"https://twitter.com/{username}/status/{tweet.id}",
                date=tweet.date,
                media_urls=[media.fullUrl for media in tweet.media] if tweet.media else []
            )
            items.append(item)

    return items
