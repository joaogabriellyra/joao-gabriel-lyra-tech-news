from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    news = find_news()

    categories = []
    for new in news:
        categories.append(new["category"])
    filtered_categories = []
    for category in Counter(sorted(categories)).most_common()[0:5]:
        filtered_categories.append(category[0])
    return filtered_categories
