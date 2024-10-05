import asyncio
from dotenv import load_dotenv
from celery import shared_task
import logging

from .models import Video, Tiktoker
from scraping.scraper import TikTokScraper, USER_AGENTS


# Load environment variables from the .env file
load_dotenv(".env", override=True)


logger = logging.getLogger(__name__)


@shared_task
def collect_data():
    print('task running')

    # Initialize the TikTok scraper
    tiktok_scraper = TikTokScraper(user_agent=USER_AGENTS[0])

    # List of keywords to scrape from TikTok
    keywords = [
        "beautiful destinations",
        "places to visit",
        "places to travel",
        "places that don't feel real",
        "travel hacks",
    ]

    # Scrape videos for each keyword and save to database
    for keyword in keywords:
        videos_data = asyncio.run(tiktok_scraper.scrape_tiktok_search(keyword))
        print(f"Number of videos scraped for '{keyword}': {len(videos_data)}")

        for video in videos_data:
            _v, _created = Video.objects.update_or_create(**video)
            print(f"Scraping user: {_v.author_username}")
            _user = asyncio.run(tiktok_scraper.scrape_tiktok_user(_v.author_username))
            _u = Tiktoker.objects.update_or_create(**_user)

    # List of hashtags to scrape from TikTok
    hashtags = [
        "#traveltok",
        "#wanderlust",
        "#backpackingadventures",
        "#luxurytravel",
        "#hiddengems",
        "#solotravel",
        "#roadtripvibes",
        "#travelhacks",
        "#foodietravel",
        "#sustainabletravel",
    ]

    # Scrape videos for each hashtag and save to database
    for hashtag in hashtags:
        videos_data = asyncio.run(tiktok_scraper.scrape_tiktok_hashtag(hashtag))
        print(f"Number of videos scraped for '{hashtag}': {len(videos_data)}")

        for video in videos_data:
            _v, _created = Video.objects.update_or_create(**video)
            print(f"Scraping user: {_v.author_username}")
            _user = asyncio.run(tiktok_scraper.scrape_tiktok_user(_v.author_username))
            _u = Tiktoker.objects.update_or_create(**_user)
