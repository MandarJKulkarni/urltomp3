import os
import requests
from gtts import gTTS
from newspaper import Article
from newspaper import fulltext
from pygame import mixer


def get_text_from_url(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as ex:
        return ex.__str__()


def mp3_from_url(input_url):
    url_text = get_text_from_url(input_url)

    html = requests.get(input_url).text
    text = fulltext(html)

    if url_text:
        mp3file = './/article.mp3'
        if os.path.exists(mp3file):
            os.remove(mp3file)
        gTTS(url_text).save(mp3file)
        return input_url
    return "Unable to extract the data from the page"


def play(mp3file):
    mixer.init()
    mixer.music.load(mp3file)
    mixer.music.play()

