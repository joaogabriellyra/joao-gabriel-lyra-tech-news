from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    filtered_news_output = []
    filtered_news = search_news({"title": {"$regex": title, "$options": "i"}})
    for new in filtered_news:
        filtered_news_output.append((new["title"], new["url"]))
    return filtered_news_output


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
