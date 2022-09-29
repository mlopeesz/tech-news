import requests
import time
from parsel import Selector


# Requisito 1
BLOG_URL = "https://blog.betrybe.com/"


def fetch(url: str):
    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content: str):
    selector = Selector(text=html_content)
    news_url = selector.css(".cs-overlay-link ::attr(href)").getall()
    return news_url


# Requisito 3
def scrape_next_page_link(html_content: str):
    selector = Selector(text=html_content)
    next_page_url = selector.css(".next.page-numbers ::attr(href)").get()
    if next_page_url:
        return next_page_url
    else:
        return None


# Requisito 4
def scrape_noticia(html_content: str):
    selector = Selector(text=html_content)
    result = {
        "url": selector.css('link[rel="canonical"]::attr(href)').get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date ::text").get(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": len(selector.css("div.comment-body").getall()),
        "summary": "".join(
            selector.css(".entry-content > p:nth-of-type(1) *::text").getall()
        ).strip(),
        "tags": selector.css("[rel=tag]::text").getall(),
        "category": selector.css(".label ::text").get(),
    }
    return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
