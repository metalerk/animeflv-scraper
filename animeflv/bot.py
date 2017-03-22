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
        main_div = self.parser.find("ul", class_="ListEpisodios AX Rows A06 C04 D03")
        cards = main_div.find_all("a", class_="fa-play")
        last_episodes_list = list()

        for card in cards:
            url = self.prefix + card['href']
            title = card.find_all("strong", class_="Title")
            title = title[0].text
            episode = card.find_all("span", class_="Capi")
            episode = episode[0].text
            episode = int(episode.split(" ")[1])
            image = card.find_all("img")
            image = self.prefix + image[0]['src']

            aux = {
                "title" : title,
                "episode" : episode,
                "image" : image,
                "url" : url
            }

            last_episodes_list.append(aux)

        return last_episodes_list