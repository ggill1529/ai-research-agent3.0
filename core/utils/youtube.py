# youtube.py – YouTube Video Fetching Utility

from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from core.schema import ResearchItem
from datetime import datetime


def fetch_youtube_videos(config):
    print("📺 Fetching YouTube videos...")
    api_key = config["api_key"]
    channel_ids = config["channel_ids"]

    youtube = build("youtube", "v3", developerKey=api_key)
    items = []

    for channel_id in channel_ids:
        request = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            order="date",
            maxResults=config.get("max_results", 5)
        )
        response = request.execute()

        for item in response.get("items", []):
            video_id = item["id"].get("videoId")
            snippet = item.get("snippet", {})

            if not video_id:
                continue

            transcript_text = ""
            try:
                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                transcript_text = " ".join([x['text'] for x in transcript])
            except TranscriptsDisabled:
                continue

            content = snippet.get("description", "") + "\n\n" + transcript_text
            research_item = ResearchItem(
                title=snippet.get("title", "No Title"),
                content=content[:3000],
                source="YouTube",
                url=f"https://youtube.com/watch?v={video_id}",
                date=datetime.strptime(snippet["publishedAt"], "%Y-%m-%dT%H:%M:%SZ"),
                media_urls=[snippet.get("thumbnails", {}).get("high", {}).get("url", "")]
            )
            items.append(research_item)

    return items
