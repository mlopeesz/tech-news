from tech_news.database import search_news


# Requisito 6
def search_by_title(title: str):
    found_news = []
    search = search_news({"title": {"$regex": f"{title.lower()}"}})
    for new in search:
        found_news.append((new["title"], new["url"]))
    return found_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    found_news = []
    search = search_news({"tags": {"$regex": tag, "$options": "i"}})
    for new in search:
        found_news.append((new["title"], new["url"]))
    return found_news


# Requisito 9
def search_by_category(category):
    found_news = []
    search = search_news({"category": {"$regex": category, "$options": "i"}})
    for new in search:
        found_news.append((new["title"], new["url"]))
    return found_news
