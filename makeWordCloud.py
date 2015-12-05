import matplotlib.pyplot as plt
import random
import re

from scipy.misc import imread
from cleanTweets import clean_text
from wordcloud import WordCloud, STOPWORDS

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

# Read the text.
with open('tweets.txt', 'rb') as f:
    tweet_list = f.readlines()

text = clean_text(tweet_list)
stopwords = STOPWORDS.copy()
stopwords.add("us")
stopwords.add("one")
stopwords.add("will")
stopwords.add("u")

wc = WordCloud(max_words=100, stopwords=stopwords, margin=10, random_state=5, width=2000, height=1200).generate(text)
#               font_path="/home/koroviev/Word Cloud Generator/Arial Unicode MS.ttf").generate(text)

fig = plt.figure(figsize=(32, 20), dpi=100)
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=1))

# Save image:
outfilename = "tmp.png"
wc.to_file(outfilename)
plt.axis("off")

plt.show()
