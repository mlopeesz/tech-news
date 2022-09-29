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
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
