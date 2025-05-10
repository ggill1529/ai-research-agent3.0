# arxiv.py – ArXiv Paper Fetching Utility

from arxiv import Client, Search, SortCriterion
from core.schema import ResearchItem


def fetch_arxiv_papers():
    print("📚 Fetching latest arXiv AI/ML papers...")
    client = Client()
    search = Search(
        query="cat:cs.AI OR cat:cs.LG",
        max_results=10,
        sort_by=SortCriterion.SubmittedDate
    )
    items = []

    for result in client.results(search):
        item = ResearchItem(
            title=result.title,
            content=result.summary,
            source="arXiv",
            url=result.pdf_url,
            date=result.published,
            media_urls=[]
        )
        items.append(item)

    return items
