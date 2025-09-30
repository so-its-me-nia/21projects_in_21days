import asyncio
import os
import json
import zipfile
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy

OUTPUT_DIR = "crawl_output"
ZIP_FILE = "crawl_results.zip"

async def main():
    config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=2,
            include_external=False,
            max_pages=300
        ),
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=True
    )

    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun("https://www.wikipedia.org", config=config)
        print(f"Crawled {len(results)} pages in total")

        os.makedirs(OUTPUT_DIR, exist_ok=True)

        for i, result in enumerate(results, 1):
            out_path = os.path.join(OUTPUT_DIR, f"page_{i}.json")
            # Convert CrawlResult to dict safely
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(result.dict(), f, indent=2, ensure_ascii=False)


        print(f"Saved all crawled pages into {OUTPUT_DIR}")

if __name__ == "__main__":
    asyncio.run(main())
