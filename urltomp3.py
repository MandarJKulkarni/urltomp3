import os
from gtts import gTTS
import trafilatura
from pygame import mixer
import logging

logger = logging.getLogger(__name__)

def gettext(url):
    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            return trafilatura.extract(downloaded)
    except Exception as ex:
        logger.error("failed to get text from url: " + url + " error: " + ex.__str__())
    return None

def getmp3(input_url):
    url_text = gettext(input_url)

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

