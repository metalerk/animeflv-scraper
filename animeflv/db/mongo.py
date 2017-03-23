from pymongo import MongoClient
import configparser
import os

class Mongo:

    def __init__(self):

        try:
            config = configparser.ConfigParser()
            config.read(os.path.abspath("../animeflv.conf"))

            # Read configuration
            DB = config['db']
            host = DB['host'] if 'host' in DB else 'localhost'
            port = int(DB['port']) if 'port' in DB else 27017
            db_name = DB['db_name'] if 'db_name' in DB else 'animeflv'

            # DB Connection
            self.__mongo = MongoClient(host=host, port=port)
            self.__database = self.__mongo[db_name]

        except Exception as err:
            print("Error: {}".format(err))
            self.__del__()

    def new_episodes(self, data=None, action="WRITE", flush=False):

        try:
            new_episodes_collection = self.__database['new_episodes']

            if "WRITE" in action and data is not None:
                new_episodes_collection.insert(doc_or_docs=data)
                return True
            elif "FIND" in action and data is not None:
                new_episodes_collection.find(data)
                return True
            elif flush and data is None:
                new_episodes_collection.delete_many({})
                return True
            else:
                return False

        except Exception as err:
            print("Error: {}".format(err))

    def search_all(self, data=None, action="WRITE", flush=False):

        try:
            search_all_collection = self.__database['search_all']

            if "WRITE" in action and data is not None:
                search_all_collection.insert(doc_or_docs=data)
                return True
            elif "FIND" in action and data is not None:
                search_all_collection.find(data)
                return True
            elif flush and data is None:
                search_all_collection.delete_many({})
                return True
            else:
                return False

        except Exception as err:
            print("Error: {}".format(err))

    def __del__(self):
        self.__mongo.close()