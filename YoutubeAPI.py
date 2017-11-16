import requests
from flask import json


def getKey():
    file = open("youtube.txt", "r")
    key = file.readline()
    file.close()
    return key

import argparse
from googleapiclient.discovery import build


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = getKey()
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options,
    part='id,snippet',
  ).execute()

  videos = []
  vids = []
  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get('items', []):
      if search_result['id']['kind'] == 'youtube#video':
        #videos.append(([search_result['snippet']['title']],[search_result['id']['videoId']]))
        title = [str(search_result['snippet']['title'])]
        id = ["https://www.youtube.com/embed/" + str(search_result['id']['videoId'])]
        video = []
        video.append(title)
        video.append(id)
        videos.append(video)
  composite_list = [videos[x:x + 3] for x in range(0, len(videos), 3)]
  return (composite_list)


  #return (vids)

#if __name__ == '__main__':
#    try:
#        videos = youtube_search("sexdfcgvhbjnkml")
#        print(videos)
#        composite_list = [videos[x:x + 3] for x in range(0, len(videos), 3)]
#        print(composite_list)
#        for i in composite_list:
#            print(i)

#    except Exception as e:
#        print(e)

