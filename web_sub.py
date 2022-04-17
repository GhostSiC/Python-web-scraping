import requests
from bs4 import BeautifulSoup

import re
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.options import Options

from urllib.request import Request, urlopen

class Anime:
    def __init__(self, name, desc, torrent, date, raw_data_img):
        self.name = name
        self.desc = desc
        self.torrent = torrent
        self.date = date
        self.raw_data_img = raw_data_img


class WebClass:
    def __init__(self, url):
        self.url = url
        self.data = []

        self.get_anime_form_list()

        for x in re.split('/', self.url):
            if "www." in x:
                self.name = x

        self.connect()

    def connect(self, delay=15):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.browser = webdriver.Chrome(executable_path="chromedriver", chrome_options=chrome_options)
        self.browser.get(self.url)

        try:
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.ID, 'releases-table')))
            self.html = self.browser.page_source
            self._soup = BeautifulSoup(self.html, "html.parser")

        except TimeoutException:
            print("Loading took too much time!")

    def close_brw(self):
        self.browser.close();

    def get_anime_by_name(self):
        list_of_anime = []

        elems = self.browser.find_elements(by=By.ID, value="releases-table")
        for tr in elems[0].find_elements(by=By.TAG_NAME, value="tr"):
            release_item = tr.find_elements(by=By.CLASS_NAME, value="release-item")[0]
            a_href_rls_item = release_item.find_elements(by=By.TAG_NAME, value="a")[0]
            name = a_href_rls_item.text

            if name.rsplit("—", 1)[0].rstrip() in self.white_list_anime:

                url_to_img = a_href_rls_item.get_attribute("data-preview-image")
                req = requests.get(url_to_img, headers={'User-Agent': 'Mozilla/5.0'})
                image_byt = req.content

                for badge_wrapper in release_item.find_elements(by=By.CLASS_NAME, value="badge-wrapper"):
                    for a in badge_wrapper.find_elements(by=By.TAG_NAME, value="a"):
                        if a.text in "1080p":
                            torret_url = a.get_attribute("href")

                release_item_time = tr.find_elements(by=By.CLASS_NAME, value="release-item-time")[0]
                span = release_item_time.find_elements(by=By.TAG_NAME, value="span")[0]
                date = span.get_attribute("title")

                list_of_anime.append(Anime(name, "mb i add that", torret_url, date, image_byt))

        return list_of_anime

    def get_anime_form_list(self):
        f = open("white_list_anime.kkk", "r")
        self.white_list_anime = []
        for line in f:
            line = line.replace("\n", '')
            self.white_list_anime.append(line)

        f.close()
