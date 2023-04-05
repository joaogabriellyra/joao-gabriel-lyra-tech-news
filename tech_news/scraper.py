import requests
from time import sleep
from parsel import Selector
from bs4 import BeautifulSoup
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, headers={"User-Agent": "Fake user-agent"}, timeout=3
            )
        sleep(1)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return None
    return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    links = selector.css("header.entry-header h2 a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next = selector.css("a.next::attr(href)").get()
    return next


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    selector = Selector(html_content)
    one_new = {}
    one_new["url"] = soup.find("link", rel="canonical").get("href")
    one_new["title"] = selector.css("div.entry-header-inner h1::text").get(

    ).strip()
    one_new["timestamp"] = selector.css("li.meta-date::text").get()
    one_new["writer"] = selector.css("span.author a::text").get()
    one_new["reading_time"] = int(selector.css(
        "li.meta-reading-time::text").re_first(r"\d+"))
    one_new["summary"] = soup.find(
        "div", {"class": "entry-content"}).p.text.strip()
    one_new["category"] = selector.css("span.label::text").get()
    return one_new


# Requisito 5
def get_tech_news(amount):
    next_page = "https://blog.betrybe.com/"
    news = []
    while next_page:
        response = fetch(next_page)
        news_links = scrape_updates(response)
        for new in news_links:
            if (amount > len(news)):
                new_to_add = scrape_news(fetch(new))
                news.append(new_to_add)
                next_page = scrape_next_page_link(response)
            else:
                next_page = None
    create_news(news)
    return news
