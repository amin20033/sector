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
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
        if response.status_code != 200:
            return []
        data = response.json()
        news_list = []
        if data.get("results"):
            for news in data["results"][:5]:
                news_list.append({
                    "title": news.get("title", "No Title"),
                    "source": news.get("source_id", "Unknown"),
                    "link": news.get("link", ""),
                    "description": news.get("description") or "No description available"
                })
        return news_list
    except Exception as e:
        print("Error fetching news:", str(e))
        return []