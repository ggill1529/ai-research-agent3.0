# report.py – Report Generator (Markdown, HTML, PDF)

import markdown2
from jinja2 import Template
from weasyprint import HTML
from core.schema import ResearchItem
from collections import defaultdict
import os


async def generate_report(items: list, timestamp: str):
    print("📄 Rendering Markdown report...")
    items_by_cluster = defaultdict(list)
    for item in items:
        cluster = getattr(item, "cluster_id", -1)
        items_by_cluster[cluster].append(item)

    markdown = f"# AI Research Report\n\nGenerated on **{timestamp}**\n\n"
    markdown += "## Executive Summary\n\n_(To be completed automatically in future iterations.)_\n\n"

    for cluster_id, cluster_items in items_by_cluster.items():
        markdown += f"## Topic Cluster {cluster_id if cluster_id >= 0 else 'Uncategorized'}\n\n"
        for item in cluster_items:
            markdown += f"### {item.title}\n"
            markdown += f"**Source**: {item.source}  |  **Date**: {item.date.strftime('%Y-%m-%d')}\n\n"
            markdown += f"{item.content}\n\n"
            markdown += f"[Read more]({item.url})\n\n"
            for media_path in item.media_urls or []:
                if media_path:
                    markdown += f"![Image]({media_path})\n\n"

    with open(f"ai_research_report_{timestamp}.md", "w", encoding="utf-8") as f:
        f.write(markdown)

    print("🌐 Generating HTML from Markdown...")
    html_body = markdown2.markdown(markdown)
    html_template = Template("""
    <html>
    <head>
        <title>AI Research Report</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 40px; line-height: 1.6; }
            h1, h2, h3 { color: #2c3e50; }
            img { max-width: 100%; height: auto; margin-top: 10px; margin-bottom: 20px; }
            a { color: #2980b9; text-decoration: none; }
        </style>
    </head>
    <body>{{ content|safe }}</body>
    </html>
    """)
    html = html_template.render(content=html_body)

    html_path = f"ai_research_report_{timestamp}.html"
    pdf_path = f"ai_research_report_{timestamp}.pdf"

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    print("🖨️ Exporting PDF report...")
    HTML(string=html).write_pdf(pdf_path)

    print(f"📁 Reports saved: {html_path}, {pdf_path}")
