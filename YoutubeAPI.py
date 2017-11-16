import requests
from flask import json


def getKey():
    file = open("youtube.txt", "r")
    key = file.readline()
    file.close()
    return key
class YouTubeSearch:
    def __init__(self):
              self.key = getKey()
        #the actual function to call for an image link, with a query
    def newVideo(self,query):
            formatedURL = "https://www.googleapis.com/customsearch/v1?key={0}" \
                     "&cx=017800523099077225978:er15x8rnv_i&q={1}&searchT" \
                     "ype=image&fileType=jpg&imgSize=medium&alt=json".format(self.key,query)

            request = requests.get(formatedURL)
            json_data = json.loads(request.content)
            print(json_data)

#GET https://www.googleapis.com/youtube/v3/search?part=id%2Csnippet&q=dog&key={YOUR_API_KEY}