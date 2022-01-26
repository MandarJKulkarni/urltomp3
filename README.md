Python package to generate mp3 for a text from content in a page from given URL using Google's text to speech package

Simple example

```
 >>> urltomp3.getmp3('https://abcd.com/article1')
 >>> urltomp3.play(./article.mp3)
```
If you just want the text, that can be done via gettext:
```
>>> article_text = urltomp3.gettext('https://abcd.com/article1')
```
