from ..database import search_news


# Requisito 7
def search_by_title(title):
    search = search_news({"title": {"$regex": title, "$options": "i"}})
    if not search:
        return []
    return [(news["title"], news["url"]) for news in search]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
