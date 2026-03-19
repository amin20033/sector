import httpx
from decouple import config

API_KEY = config("API_KEY")

async def fetch_news(sector):
    """
    Fetch top 5 news for a given sector from NewsData.io API.
    """
    url = "https://newsdata.io/api/1/news"
    params = {
        "apikey": API_KEY,
        "q": sector
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        data = response.json()

    news_list = []
    if data.get("results"):
        for news in data["results"][:5]:  # top 5 news
            news_list.append({
                "title": news.get("title"),
                "source": news.get("source_id"),
                "link": news.get("link"),
                "description":news.get("description")
            })
    return news_list