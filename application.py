import time
from flask import Flask, request, render_template, send_file

# from bson.objectid import ObjectId
# from scrapper import Scrapper
from mongo_operation import MongoOperation
from ytutils import YtUtils

application = Flask(__name__)
app = application

channel_ids = ['UCNU_lfiiWBdtULKOw6X0Dig', 'UCb1GdqUqArXMQ3RS86lqqOw', 'UCDrf0V4fcBr5FlCtKwvpfwA']

@app.route("/")
def home():
    channels = []
    mo = MongoOperation()
    ytu = YtUtils()
    for id in channel_ids:
        channel = ytu.get_channel_details(id)
        channels.append(channel)
    mo.save_channels(channels)
    return render_template("index.html", channels=channels)

@app.route("/find", methods=('POST',))
def find():
    if request.method == "POST":
       url = request.form.get("url")
       video_id = url.split("=")[-1]
       ytu = YtUtils()
       mo = MongoOperation()
       video_details = mo.get_video_details(video_id)
       if video_details is None:
        video_details = ytu.get_video_details(video_id)
        if video_details is not None:
            mo.save_video(video_details)
        else:
            video_details = False
       
    return render_template("video_details.html", video=video_details)

# def home():
#     channels = []
#     mo = MongoOperation()
#     ytu = YtUtils()
#     # moc = mo.get_collection(collection_name='youtubechannel')
#     # channel = ytu.get_channel_details(channel_ids[1])
#     # channels.append(channel)
#     for id in channel_ids:
#         # channel = ytu.get_channel_details(id)
#         # channels.append(channel)
#         # time.sleep(3)
#         channel = mo.get_channel_details(id)
#         if channel is not None:
#             channels.append(channel)
#         # else:
#             # channel = ytu.get_channel_details(id)
#             # mo.save_channel(channel)
#             # channels.append(channel)
#     # mo.save_channels(channels)
#     return render_template("index.html", channels=channels)
#     # return render_template("index.html")


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)

