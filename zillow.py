import requests
from bs4 import BeautifulSoup

class Zillow:
    def __init__(self, url, headers):
        self.response = requests.get(url=url, headers=headers)
        self.soup = BeautifulSoup(self.response.text, features="html.parser")

    def find_links(self):
        links_scraped = self.soup.find_all(attrs={"data-test": "property-card-link"})
        links = []
        for link in links_scraped:
            href = link.get("href")
            if 'http' in href:
                links.append(href)
            else:
                links.append(f"https://www.zillow.com{href}")
        return list(dict.fromkeys(links)) #to remove duplicates

    def find_prices(self):
        prices_scraped = self.soup.find_all(attrs={"data-test": "property-card-price"})
        price_list = [price.get_text().split("+")[0] for price in prices_scraped]
        return price_list

    def find_addresses(self):
        address_scraped = self.soup.find_all(attrs={"data-test": "property-card-addr"})
        address_list = [address.get_text() for address in address_scraped]
        return address_list