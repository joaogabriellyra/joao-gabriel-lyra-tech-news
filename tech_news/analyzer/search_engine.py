from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    filtered_news_output = []
    filtered_news = search_news({"title": {"$regex": title, "$options": "i"}})
    for new in filtered_news:
        filtered_news_output.append((new["title"], new["url"]))
    return filtered_news_output


# Requisito 8
def search_by_date(date):
    try:
        filtered_news_output = []
        date_to_filter = datetime.strptime(date, "%Y-%m-%d").date()
        new_date = date_to_filter.strftime("%d/%m/%Y")
        filtered_news = search_news({"timestamp": {"$regex": new_date}})
        for new in filtered_news:
            filtered_news_output.append((new["title"], new["url"]))
        return filtered_news_output
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    filtered_news_output = []
    filtered_news = search_news(
        {"category": {"$regex": category, "$options": "i"}})
    for new in filtered_news:
        filtered_news_output.append((new["title"], new["url"]))
    return filtered_news_output
