import time
import tweepy
import requests
import json
import urllib.request
import os
import uuid


# Authenticate to Twitter
auth = tweepy.OAuthHandler("bej18ws1jYL2pOhRdKo4zgQE3",
                           "kyBAEEDwYQZcPPUUb2KPe2zCHapRtjz4fvQQZyv0wGN2OOCWbE")
#
auth.set_access_token("1162051959316107264-2PZvYPonct6zC0llIHqYzwzetqu6qc",
                      "W2lAcO57hBJs3iMz2i8hsJqUpAmjQzIYARN3TNsclUrth")

# Create API object
api = tweepy.API(auth)

dirName: str = 'images'
useAgent: str = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'


def getNameExt(url: str) -> str:
    return url.split(".").pop()


def getMemes() -> list:
    r = requests.get('https://meme-api.herokuapp.com/gimme/2')
    data = json.loads(r.text)
    return data['memes']


def postMeme(meme):
    api.update_with_media(f'{dirName}/{meme}')


def postMemes(memes: list):
    for meme in memes:
        time.sleep(300)  # Sleep 5 minutes
        postMeme(meme)


def downloadMeme(url: str):
    os.makedirs(dirName, exist_ok=True)
    name: str = f'{uuid.uuid1()}.{getNameExt(url)}'
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', useAgent)]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url, f"{dirName}/{name}")


def reset(dlMemes: list):
    for f in dlMemes:
        os.remove(f'{dirName}/{f}')


def init():
    memes: list = getMemes()
    for meme in memes:
        downloadMeme(meme['url'])
    dlMemes = os.listdir(dirName)
    try:
        postMemes(dlMemes)
    except:
        time.sleep(1200)  # Sleep 20 minutes
        print('something went wrong')
    reset(dlMemes)


init()
