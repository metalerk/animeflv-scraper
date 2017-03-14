import requests
import cfscrape
from bs4 import BeautifulSoup

class BotAnimeFLV:
    def __init__(self, url="animeflv.net"):
        self.url = url
        self.scraper = cfscrape.create_scraper()
        self.main_html = self.scraper.get("http://animeflv.net/")
        self.parser = BeautifulSoup(self.main_html.content, 'html.parser')
        self.prefix = "http://animeflv.net"

    def get_last_episodes(self):
        main_div = self.parser.find_all("a", class_="fa-play")
        last_episodes_list = list()

        for card in main_div:
            serie = dict()
            image_span = card.find_all("span", class_="Image")
            print(image_span)
            #image_metadata = image_span.find_all("img")

            #image = image_metadata[0]

            #serie['image'] = self.prefix + image['src']
            #serie['title'] = image['alt']

            last_episodes_list.append(serie)

        return last_episodes_list