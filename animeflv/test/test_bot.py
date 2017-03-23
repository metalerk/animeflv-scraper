import unittest
from animeflv.bot import BotAnimeFLV
from pprint import pprint
import json
class TestBot(unittest.TestCase):

    def test_get_last_episodes(self):
        bot = BotAnimeFLV()
        last_episodes = bot.get_last_episodes()
        self.assertEqual(type(last_episodes), list)
        self.assertGreater(last_episodes.__len__(), 0)
        #response = json.dumps(last_episodes)
        pprint(last_episodes)

if __name__ == '__main__':
    unittest.main()
