import time
import tweepy
import requests
import json
import urllib.request
import os
import uuid


# Authenticate to Twitter
auth = tweepy.OAuthHandler("API_KEY",
                           "API_SECRET")
#
auth.set_access_token("ACCESS_TOKEN",
                      "ACCESS_TOKEN_SCRET")

# Create API object
api = tweepy.API(auth)

dirName: str = 'images'


def getNameExt(url: str) -> str:
    return url.split(".").pop()


def getMemes() -> list:
    print('Getting memes from API')
    r = requests.get('https://meme-api.herokuapp.com/gimme/30')
    data = json.loads(r.text)
    return data['memes']


def postMeme(meme):
    print(f'Posting meme - {meme}')
    try:
        api.update_with_media(f'{dirName}/{meme}')
    except Exception as e:
        print('Somethign went wrong while posting')
        print(e)


def postMemes(memes: list):
    for meme in memes:
        time.sleep(300)  # Sleep 5 minutes
        postMeme(meme)


def downloadMeme(url: str):
    os.makedirs(dirName, exist_ok=True)
    name: str = f'{uuid.uuid1()}.{getNameExt(url)}'
    opener = urllib.request.build_opener()
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
    except Exception as e:
        time.sleep(1200)  # Sleep 20 minutes
        print('Something went wrong')
        print(e)
    reset(dlMemes)


while True:
    init()
