import requests
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/Washington_(state)"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


def get_citations_needed_count(url):
    all_citations_needed = soup.find_all("a", title="Wikipedia:Citation needed")
    # print(all_citations_needed)
    return len(all_citations_needed)


def get_citations_needed_report(url):
    cites = soup.find_all("a", title="Wikipedia:Citation needed")
    for cite in cites:
        parent_p = cites.find_parent("p")
        content = parent_p
    print(content, end="\n" * 6)


print(get_citations_needed_count(url))
get_citations_needed_report(url)
