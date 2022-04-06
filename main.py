import bs4
import requests
from bs4 import BeautifulSoup
import os
import texttable as tt
import re

class web_class:
    def __init__(self, url):
        self.url = url
        self._page = requests.get(url)
        self._soup = BeautifulSoup(self._page.content, "html.parser")
        self.data = []

        for x in re.split('/', self.url):
            if "www." in x:
                self.name = x

    def print_data(self):
        table = tt.Texttable()
        table.add_rows([(None,None,None,None)] + self.data)

        table.set_cols_align(("c","c","c","c"))
        table.header(("Country", "Cases", "Death", "Region"))
        print(f'web site name: {self.name}')
        print(table.draw()) 

    def change_url(self, url):
        self.url = url

    def get_all_data(self):
        res = iter(self._soup.find_all('td'))
        while True:
            try:
                country = next(res).text
                cases = next(res).text
                death = next(res).text
                region = next(res).text

                self.data.append((
                    country,
                    cases.replace(",", ''),
                    death.replace(",", ''),
                    region
                ))
            except StopIteration:
                break

    def query_country_by_name(self, *args):
        res = iter(self._soup.find_all('td'))

        #tab_html = self._soup.find("div", class_="table-responsive")
        #print(tab_html.find_all('td'))

        while True:
            try:
                country = next(res).text
                cases = next(res).text
                death = next(res).text
                region = next(res).text
                for arg in args:
                    if country == arg:
                        self.data.append((
                            country,
                            cases.replace(",", ''),
                            death.replace(",", ''),
                            region
                        ))
            except StopIteration:
                break
           



if __name__ == "__main__":
    os.system("CLS")
    web = web_class("https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/")
    web.query_country_by_name("Saint Helena","Marshall Islands")
    web.query_country_by_name("Micronesia","Poland")
    web.print_data()   
    web.data = []