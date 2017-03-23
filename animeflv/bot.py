import configparser
import cfscrape
import os
from bs4 import BeautifulSoup
import base64

class BotAnimeFLV:
    def __init__(self, url="animeflv.net"):
        self.config = configparser.ConfigParser()
        self.config.read("../animeflv.conf")
        self.url = url
        self.scraper = cfscrape.create_scraper()
        self.main_html = self.scraper.get("http://animeflv.net")
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
                "watch" : url
            }

            last_episodes_list.append(aux)

        return last_episodes_list

    def search_all(self):
        genres_config = self.config['genres']
        genres_list = genres_config['genres'].replace(" ", "").replace("\n", "").split(",")
        data = list()
        for genre in genres_list:
            print(genre)
            data.append(self.search_by_genre(genre=genre))

        return data


    def search_by_genre(self, genre):
        base_search_url = self.prefix + "/browse?genre[]=" + genre
        genre_page = self.scraper.get(base_search_url)
        parser = BeautifulSoup(genre_page.content, 'html.parser')
        pagination = parser.find("ul", class_="pagination")
        pagination_items = pagination.find_all("li")
        if pagination_items.__len__() > 1:
            last_page = pagination_items.__len__() - 2
        else:
            last_page = 1

        #last_page = int(pagination.find_all("li")[-2].text)
        data = dict()
        data_aux = list()

        counter = 0

        for page in range(1, last_page + 1):
            current_page = self.scraper.get(base_search_url + '&page=' + str(page))
            parser = BeautifulSoup(current_page.content, 'html.parser')
            cards_div = parser.find_all("ul", class_="ListAnimes AX Rows A03 C02 D02")

            for card_div in cards_div:
                cards = card_div.find_all("li")
                for card in cards:
                    info_text = card.find("div", class_="Text")
                    info = info_text.find("h3", class_="Title")
                    watch = self.prefix + info.find("a")['href']
                    title = info.text
                    description = info_text.find("p").text
                    image = self.prefix + card.find("img")['src']
                    type = card.find("span").text
                    additional_genres = card.find("div", class_="Tags")
                    additional_genres = [genre.text.lower() for genre in additional_genres.find_all("a")]

                    data_aux.append({
                        "title" : title,
                        "type" : type,
                        "description" : description,
                        "image" : image,
                        "genres" : additional_genres,
                        "watch" : watch
                    })

                    counter += 1

        data['genre'] = genre
        data['total'] = counter
        data['content'] = data_aux

        return data