import os
from gtts import gTTS
from newspaper import Article


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

    if url_text:
        mp3file = './/article.mp3'
        if os.path.exists(mp3file):
            os.remove(mp3file)
        gTTS(url_text).save(mp3file)
        return input_url
    return "Unable to extract the data from the page"
