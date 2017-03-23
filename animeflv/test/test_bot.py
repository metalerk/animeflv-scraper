import unittest
from animeflv.bot import BotAnimeFLV
from pprint import pprint
import json
import datetime
from animeflv.db.mongo import Mongo

class TestBot(unittest.TestCase):
    """

    def test_get_last_episodes(self):
        bot = BotAnimeFLV()
        last_episodes = bot.get_last_episodes()
        self.assertEqual(type(last_episodes), list)
        self.assertGreater(last_episodes.__len__(), 0)
        #response = json.dumps(last_episodes)
        pprint(last_episodes)

    def test_search_by_genre(self):
        bot = BotAnimeFLV()
        data = list()
        genres = ["militar", "magia", "misterio"]
        start = datetime.datetime.now()
        for genre in genres:
            res = bot.search_by_genre(genre=genre)
            data.append(res)

        end = datetime.datetime.now()
        diff = end - start
        pprint(data)
        print(diff)
        """

    def test_search_all(self):
        print("SEARCH ALL...")
        bot = BotAnimeFLV()
        start = datetime.datetime.now()
        data = bot.search_all()
        end = datetime.datetime.now()
        diff = end - start
        pprint(data)
        total = sum([obj['total'] for obj in data])
        print(total)
        print(diff)
        mongo = Mongo()
        self.assertTrue(mongo.search_all(data=data, action="WRITE"))

if __name__ == '__main__':
    unittest.main()
