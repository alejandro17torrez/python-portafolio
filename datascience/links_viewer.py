"""
This script is for get all links of a homepage web site or any web page
"""

import os
from urllib.request import Request, urlopen

import validators
from bs4 import BeautifulSoup


class WebInfo:
    def __init__(self, url, sitename, filename="links") -> None:
        self.url = url
        self.filename = filename
        self.sitename = sitename

    def get_links(self):
        if self.validate_urls():
            request_site = Request(url=self.url, headers={"User-Agent": "Mozilla/5.0"})
            webpage_info = urlopen(request_site)
            bs = BeautifulSoup(webpage_info.read(), "html.parser")
            webpage_info.close()

            webpage_links = [
                link.get("href") for link in bs.find_all("a") if link.get("href")
            ]

            with open(f"{self.sitename}_{self.filename}.txt", "w") as data_file:
                counter: int = 0
                for link in webpage_links:
                    data_file.write(link + "\n")
                    counter += 1
                data_file.write(f"Count of links: {counter} \n")
        if os.path.isfile(self.filename):
            return True
        return False

    def validate_urls(self):
        return validators.url(self.url)


muj_web_site = WebInfo(input("add website: "), input("nombre del sitio: "))
muj_web_site.get_links()
