import requests
import logging

from vars import KEY
from yturls import get_channel_url, get_video_url, get_comment_url

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

class YtUtils:
    def get_channel_details(self, channel_username):
        try:
            ch_url = get_channel_url(channel_username, KEY)
            ch_response = requests.get(ch_url)
            channel_data = ch_response.json()
            channel_info = {
                '_id':channel_username,
                'channelName': channel_data['items'][0]['snippet']['title']
            }
            channel_info.update(channel_data['items'][0]['statistics'])
            return channel_info
        except Exception as e:
            logging.error(str(e))
            return None

    def get_video_details(self, video_id):
        try:
            video_url = get_video_url(video_id, KEY)
            comment_url = get_comment_url(video_id, KEY)
            video_details = {
                '_id': video_id
            }
            video_stat = requests.get(video_url).json()
            if video_stat['pageInfo']['totalResults'] == 0:
                return None
            try:
                video_details['channelName']=video_stat['items'][0]['snippet']['channelTitle']
            except Exception:
                video_details['channelName'] = ''
            try:
                video_details['title'] = video_stat['items'][0]['snippet']['title']
            except Exception:
                video_details['title'] = ''

            try:
                video_details['description'] = video_stat['items'][0]['snippet']['description']
            except Exception:
                video_details['description'] = ''

            try:
                video_details['postedOn'] = video_stat['items'][0]['snippet']['publishedAt']
            except Exception:
                video_details['postedOn'] = ''
            
            try:
                video_details.update(video_stat['items'][0]['statistics'])
            except Exception as e:
                logging(str(e))
                
            try:
                video_details['duration'] = video_stat['items'][0]['contentDetails']['duration']
            except Exception:
                video_details['duration'] = ''

            try:
                video_details['thumbnail'] = video_stat['items'][0]['snippet']['thumbnails']['standard']['url']
            except Exception:
                video_details['thumbnail'] = ''

            try:
                video_details['tags'] = video_stat['items'][0]['snippet']['tags'][1:]
            except Exception:
                video_details['tags'] = []
            
            try:
                video_details['language'] = video_stat['items'][0]['snippet']['defaultAudioLanguage']
            except Exception:
                video_details['language'] = ''

            try:
                comment_data = requests.get(comment_url).json()
                comments = []
                for comment in comment_data["items"]:
                    temp = {
                        'author': comment['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                        'comment': comment['snippet']['topLevelComment']['snippet']['textDisplay'],
                        'time': comment['snippet']['topLevelComment']['snippet']['publishedAt'],
                    }
                    reply =[]
                    if comment.get('replies'):
                        com = comment.get('replies').get('comments')
                        for c in com:
                            reply_temp = {
                                'author': c['snippet']['authorDisplayName'],
                                'comment': c['snippet']['textDisplay'],
                                'time': c['snippet']['publishedAt']
                            }
                            reply.append(reply_temp)
                    temp['reply'] = reply
                    comments.append(temp)
                video_details['comments'] = comments
            except Exception as e:
                logging(str(e))
                video_details['comments'] = []
            return video_details
        except Exception as e:
            logging.error(str(e))
            return None