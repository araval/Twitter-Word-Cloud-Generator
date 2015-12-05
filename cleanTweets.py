import re

def deal_with_unicode(line):

    line = re.sub('\xe2\x80\x99', "'", line)
    line = re.sub('\xe2\x80\xa6', "...", line)
    line = re.sub("\xc2\xb4", "'", line)
    line = re.sub('\xe2\x80\x9d', '"', line)
    line = re.sub('\xe2\x80\x94', '-', line)
    line = re.sub("\xe2\x80\x9c", '"', line)
    line = re.sub("\xe2\x80\x93", '-', line)
    line = re.sub("\xe2\x80\x95", '-', line)
    line = re.sub("\xe2\x80\x98", "'", line)
    line = re.sub("\xc2\xa0", "", line) # not sure what this is, looks like white space
    line = re.sub("\xe2\x80\x8e", "", line)
    line = re.sub("\xe2\x80\x8f", "", line)
    line = re.sub("\xc2\xba", "symbolDEGREES", line)
    line = re.sub("\xc2\xa3", 'symbolPOUNDS', line)
    line = re.sub("\xe2\x82\xac", 'symbolEURO', line)
    line = re.sub(' @ ', ' at ', line)
    line = re.sub('&amp;', ' and ', line)

    return line

def make_substitutions(line):
    line = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', line)
    try:
        line = line.decode("utf-8", "ignore")
    except UnicodeDecodeError as e:
        print 'Warning, encountered UnicodeDecodeError', e
        print line
    return line

def clean_text(tweetList):
    # text is a line of tweets
    cleantext = []
    for tweet in tweetList:
        if not tweet.startswith('RT'):
            goodwords = [word for word in tweet.split() if '@' not in word]
            tweet = ' '.join(goodwords)
            tweet = deal_with_unicode(tweet)
            tweet = make_substitutions(tweet)
            cleantext.append(tweet)

    text = ' '.join(cleantext)
    return text
