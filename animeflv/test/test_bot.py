import unittest
from animeflv.bot import BotAnimeFLV


class TestBot(unittest.TestCase):

    def test_get_last_episodes(self):
        bot = BotAnimeFLV()
        last_episodes = bot.get_last_episodes()
        print(last_episodes)

if __name__ == '__main__':
    unittest.main()
