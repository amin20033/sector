import ollama

def analyze_market(sector, news_list):
    news_text = "\n".join(news_list)

    prompt = f"""
    You are a financial analyst.

    Analyze Indian {sector} sector.

    News:
    {news_text}

    Generate markdown report with:
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