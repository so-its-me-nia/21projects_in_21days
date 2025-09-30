import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

from browser_use import Agent, ChatGoogle  


async def main():
    # Instantiate the Google Gemini model
    llm = ChatGoogle(model="gemini-2.0-flash")
    task = "Search Google for 'weirdest fictional characters in classic literature' and summarize the top 5 results with links."
    agent = Agent(task=task, llm=llm)

    result = await agent.run()

    urls = agent.history.urls()
    print("\n---------------------\nVisited URLs:")
    print(urls)

    # Save URLs to a text file
    with open("Visited_urls.txt", "w", encoding="utf-8") as f:
        for url in urls:
            f.write(url + "\n")

    print("\nVisited_urls.txt created successfully.")


if __name__ == "__main__":
    asyncio.run(main())