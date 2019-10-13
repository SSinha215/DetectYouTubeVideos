import time
import json
import urllib
from selenium import webdriver #pip install selenium for this package to work

def detect_new_video():

    api_key = "Get your api key from here: https://console.developer.google.com"
    channel_id = "Get the channel id of the youtube channel"

    base_video_url = "https://www.youtube.com/watch?v="
    base_search_url = "https://www.googleapis.com/youtube/v3/search?"

    url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=data&maxResults=1'.format(api_key,channel_id)
    inp = urllib.urloppen(url)
    resp = json.load(inp)

    vidId = resp['items'][0]['id']['videoId']

    video_exists = False
    with open('videoid.json','r') as json_file:
        data = json.load(json_file)
        if data['videoId'] != vidId:
            driver = webdriver.Firefox()
            driver.get(base_video_url + vidId)
            video_exists = True

    if video_exists:
        with open('videoid.json','w') as json_file:
            data = {'videoId': vidId}
            json.dump(data,json_file)

try:

    while True:
        detect_new_video()
        time.sleep(10)

except KeyboardInterrupt:
    print("stopping")





