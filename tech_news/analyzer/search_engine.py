from ..database import search_news
from datetime import datetime as d


# Requisito 7
def search_by_title(title):
    search = search_news({"title": {"$regex": title, "$options": "i"}})
    if not search:
        return []
    return [(news["title"], news["url"]) for news in search]


# Requisito 8
def search_by_date(date):
    try:
        formatted_date = d.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")
    search_result = search_news({"timestamp": formatted_date})
    if not search_result:
        return []
    return [(news["title"], news["url"]) for news in search_result]


# Requisito 9
def search_by_category(category):
    search = search_news({
        "category": {"$regex": category, "$options": "i"}
        })
    if not search:
        return []
    return [(news["title"], news["url"]) for news in search]
