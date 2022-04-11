
from bs4 import BeautifulSoup

import texttable as tt
import re
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class web_class:
    def __init__(self, url):
        self.url = url
        self.data = []

        for x in re.split('/', self.url):
            if "www." in x:
                self.name = x

        self.connect()

    def connect(self, delay=15):

        self.browser = webdriver.Chrome(executable_path="chromedriver")
        self.browser.get(self.url)

        try:
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.ID, 'releases-table')))
            #print(myElem)
            self.html = self.browser.page_source

            self._soup = BeautifulSoup(self.html, "html.parser")

        except TimeoutException:
            print("Loading took too much time!")


    def print_data(self):
        table = tt.Texttable()
        table.add_rows([(None, None, None, None)] + self.data)

        table.set_cols_align(("c", "c", "c", "c"))
        table.header(("Country", "Cases", "Death", "Region"))
        print(f'web site name: {self.name}')
        print(table.draw())

    def change_url(self, url):
        self.url = url

    def close_brw(self):
        self.browser.close();

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

        elems = self.browser.find_elements(by=By.CLASS_NAME, value="frontpage-releases-container")
        for i in elems[0].find_elements(by=By.CLASS_NAME, value="badge-wrapper"):
            for a in i.find_elements(by=By.TAG_NAME, value="a"):
                if a.text in "1080p":
                    print(a.text)
                    print(a.get_attribute("href")) 
                    pass





        div_tab_cointtener = self._soup.find("table", {"id": "releases-table"})
        #print(div_tab_cointtener.find_all('tr'))
        #print(div_tab_cointtener.find_all('tr'))
        #tab_html = div_tab_cointtener.find_all("table", class_="releases-table")
        for i in div_tab_cointtener.find_all('tr'):
            for a in i.find_all("a"):
                #for quality in a.find_all("div", {"class":"badge-wrapper"}):

                #print(a)

                pass


