from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title: str):
    found_news = []
    search = search_news({"title": {"$regex": f"{title.lower()}"}})
    for new in search:
        found_news.append((new["title"], new["url"]))
    return found_news


# Requisito 7
def search_by_date(date: str):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        data_iso = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        search = search_news({"timestamp": data_iso})
        return[(new["title"], new["url"]) for new in search]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag: str):
    found_news = []
    search = search_news({"tags": {"$regex": tag, "$options": "i"}})
    for new in search:
        found_news.append((new["title"], new["url"]))
    return found_news


# Requisito 9
def search_by_category(category: str):
    found_news = []
    search = search_news({"category": {"$regex": category, "$options": "i"}})
    for new in search:
        found_news.append((new["title"], new["url"]))
    return found_news
