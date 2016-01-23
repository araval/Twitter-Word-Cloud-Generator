import matplotlib.pyplot as plt
import random
import re
import sys

from scipy.misc import imread
from cleanTweets import clean_text
from wordcloud import WordCloud, STOPWORDS


def generate_wordcloud(text):

    def my_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        '''
        To change colors change the range for random ints below:
        Hue values are between 0 and 360
        Follows rainbow: 
        Red Orange Yellow Green Blue Indigo Violet
         0   50  100  150  200  250  300   360
        '''
        hue_lower = 0      
        hue_upper = 150     
        
        saturation = 500    

        light_lower = 80
        light_upper = 120

        return "hsl(%d, %d%%, %d%%)" % (random.randint(hue_lower, hue_upper), saturation, \
                                        random.randint(light_lower, light_upper))

    stopwords = STOPWORDS.copy()
    stopwords.add("us")
    stopwords.add("one")
    stopwords.add("will")
    stopwords.add("u")

    rand_num = random.randint(1,100)

    wc = WordCloud(max_words=100, stopwords=stopwords, margin=10, random_state=rand_num,\
                        width=2000, height=1200).generate(text)

    fig = plt.figure(figsize=(32, 20), dpi=100)
    plt.imshow(wc.recolor(color_func=my_color_func, random_state=1))

    # Save image
    outfilename = "tmp.png"
    wc.to_file(outfilename)
    plt.axis("off")

    plt.show()

if __name__ == "__main__":

    with open("tweets.txt", 'rb') as f:
        tweet_list = f.readlines()

    clean_tweets = clean_text(tweet_list)
    generate_wordcloud(clean_tweets)
