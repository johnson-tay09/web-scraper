import requests
from bs4 import BeautifulSoup

# assert requests
# assert BeautifulSoup

my_url = "https://en.wikipedia.org/wiki/Washington_(state)"


def soup_helper(url):
    # bring url requests into beautiful soup format
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def get_citations_needed_count(url):
    # count the number of instances of a tag containing the title of citation needed
    soup = soup_helper(url)
    all_citations_needed = soup.find_all("a", title="Wikipedia:Citation needed")
    return len(all_citations_needed)


def get_citations_needed_report(url):
    # return the parent element of the citation needed a tag, in this case they are p elements
    soup = soup_helper(url)
    cites = soup.find_all("a", title="Wikipedia:Citation needed")
    cn_content = ""
    for cite in cites:
        parent_p = cite.find_parent("p")
        cn_content += parent_p.text + "\n"
    return cn_content


print(get_citations_needed_count(my_url))
print(get_citations_needed_report(my_url))
