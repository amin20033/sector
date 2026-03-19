import ollama
def analyze_market(sector, news_list):
    formatted_news = "\n\n".join(
        f"Title: {n.get('title')}\n"
        f"Source: {n.get('source')}\n"
        f"Description: {n.get('description')}"
        for n in news_list
    )
    prompt = f"""
    You are a financial analyst.

    Analyze the Indian {sector} sector using the news below.

    News:
    {formatted_news}

    Generate a structured markdown report with:
    - Overview
    - Current Trends
    - Opportunities
    - Risks
    - Conclusion
    """
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]