# WL First Commit
import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    header = {
        "user-agent": "Fake user-agent"
    }
    try:
        response = requests.get(url, headers=header, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None
    finally:
        time.sleep(1)


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    return [news.css("a::attr(href)").get() for news
            in selector.css(".cs-overlay")]


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css("a.next::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    return {
        "url": selector.css("div::attr(data-share-url)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("span.author a::text").get(),
        "reading_time": int(
            selector.css("li.meta-reading-time::text")
            .get()
            .split()[0]
        ),
        "summary": "".join(
            selector.css(".entry-content > p:first-of-type *::text").getall()
            ).strip(),
        "category": selector.css("span.label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
