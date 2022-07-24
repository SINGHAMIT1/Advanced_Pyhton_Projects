# importing Libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os

# getting the article
article = Article("https://medium.com/@Data-Science-Course/best-5-online-data-science-courses-in-2022-c20652679ba4")

# downloading the article and parsing
article.download()
article.parse()

# downloading the punkt package and applying Natural Language processing on it
nltk.download("punkt")
article.nlp()

# Get the articles text
my_text = article.text

# choosing the language of speech
language = "en"

# passing the text and language to the engine

my_obj = gTTS(text=my_text, lang=language, slow=False)
my_obj.save("read_article.mp3")

# playing the converted audio file from text to speech by "start" command
os.system("start read_article.mp3")
