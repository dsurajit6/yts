import pymongo
import logging
from bson.objectid import ObjectId


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

class MongoOperation:
    def __init__(self, username="YOUR_USERNAME", password="YOUR_PASSWORD"):
        try:
            self. username = username
            self.password = password
            self.url = f"mongodb+srv://{username}:{password}@clusterofsurajit.99hrrkq.mongodb.net/?retryWrites=true&w=majority"
        except Exception as e:
            logging.error(str(e))
    
    def get_mongo_client(self):
        try:
            client = pymongo.MongoClient(self.url)
            return client
        except Exception as e:
            logging.error(str(e))
    
    def get_database(self, db_name="ineuron"):
        try:
            client = self.get_mongo_client()
            database = client[db_name]
            return database
        except Exception as e:
            logging.error(str(e))
    
    def get_collection(self, db_name="ineuron", collection_name="youtubevideos"):
        try:
            database = self.get_database(db_name)
            collection = database[collection_name]
            return collection
        except Exception as e:
            logging.error(str(e))
    
    def is_channel_available(self, channel_id):
        pass

    def is_video_available(self, video_id):
        pass

    def get_channel_details(self, channel_id):
        try:
            moc = self.get_collection(collection_name='youtubechannels')
            return moc.find_one({"_id": channel_id})
        except Exception as e:
            logging.error(str(e))


    def get_video_details(self, video_id):
        try:
            moc = self.get_collection(collection_name='youtubevideo')
            return moc.find_one({"_id": video_id})
        except Exception as e:
            logging.error(str(e))
    
    def save_channel(self, channel_details):
        pass

    def save_channels(self, channels):
        try:
            moc = self.get_collection(collection_name='youtubechannels')
            moc.drop()
            moc.insert_many(channels)
        except Exception as e:
            logging.error(str(e))

    def save_video(self, video_details):
        try:
            moc = self.get_collection(collection_name='youtubevideo')
            moc.insert_one(video_details)
        except Exception as e:
            logging.error(str(e))

