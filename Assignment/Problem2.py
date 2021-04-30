import os
from TrieFinal import Trie
import plotly.graph_objects as go
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
import plotly.express as px

stopword = Trie()

positiveword = Trie()
negativeword = Trie()


def eliminate_stop_word(wordlist):
    wrd = []
    for i in wordlist:
        if not stopword.search(i):
            wrd.append(i)
    return wrd
    # count stopword sekali


def word_list_frequency(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist, wordfreq)))


def eliminate_except_letters_number(word):
    import re
    wrd = []
    for i in word:
        s = re.sub(r'[^a-zA-Z0-9]', '', i)
        wrd.append(s)
    return wrd


def count_positive_percentage(worddic):
    positive = 0
    all_words = 0
    worddic_keys, worddic_values = worddic.keys(), worddic.values()
    worddic_keys = list(worddic_keys)
    worddic_values = list(worddic_values)
    for i in range(len(worddic_keys)):
        all_words += worddic_values[i]
        if positiveword.search(worddic_keys[i]):
            positive += worddic_values[i]
    positive = positive/all_words*100
    return (round(positive, 2))

# def count_positive(worddic):
#     positive = 0
#     all_words = 0
#     worddic_keys, worddic_values = worddic.keys(), worddic.values()
#     worddic_keys = list(worddic_keys)
#     worddic_values = list(worddic_values)
#     for i in range(len(worddic_keys)):
#         all_words += worddic_values[i]
#         if positiveword.search(worddic_keys[i]):
#             positive += worddic_values[i]
#     return (positive)

def count_negative_percentage(worddic):
    negative = 0
    all_words = 0
    worddic_keys, worddic_values = worddic.keys(), worddic.values()
    worddic_keys = list(worddic_keys)
    worddic_values = list(worddic_values)
    for i in range(len(worddic_keys)):
        all_words += worddic_values[i]
        if negativeword.search(worddic_keys[i]):
            negative += worddic_values[i]
    negative = negative/all_words*100
    return (round(negative, 2))

# def allword(worddic):
#     all_words = 0
#     worddic_keys, worddic_values = worddic.keys(), worddic.values()
#     worddic_keys = list(worddic_keys)
#     worddic_values = list(worddic_values)
#     for i in range(len(worddic_keys)):
#         all_words += worddic_values[i]
#     return(all_words)

# def count_negative(worddic):
#     negative = 0
#     all_words = 0
#     worddic_keys, worddic_values = worddic.keys(), worddic.values()
#     worddic_keys = list(worddic_keys)
#     worddic_values = list(worddic_values)
#     for i in range(len(worddic_keys)):
#         all_words += worddic_values[i]
#         if negativeword.search(worddic_keys[i]):
#             negative += worddic_values[i]
#     return (negative)


with open('stopwords.txt', 'r', encoding='utf-8') as f:
    f_contents = f.read()
    word = f_contents.split()
    for i in word:
        stopword.insert(i)

with open('positivewords.txt', 'r', encoding='utf-8') as f:
    f_contents = f.read()
    pwrd = f_contents.lower()
    pwrd = pwrd.replace(" ", "")
    pwrd = pwrd.split(",")
    pwrd = eliminate_except_letters_number(pwrd)
    for i in pwrd:
        positiveword.insert(i)


with open('negativewords.txt', 'r', encoding='utf-8') as f:
    nwrd = []
    f_contents = f.readlines()
    for i in f_contents:
        i = i.replace(" ", "")
        i = i.split(",")
        for j in i:
            nwrd.append(j)
    nwrd = eliminate_except_letters_number(nwrd)
    for i in nwrd:
        negativeword.insert(i)
article_arr = ["citylink1.txt", "citylink2.txt", "citylink3.txt","poslaju1.txt", "poslaju2.txt", "poslaju3.txt", "gdex1.txt", "gdex2.txt", "gdex3.txt","jnt1.txt", "jnt2.txt", "jnt3.txt", "dhl1.txt","dhl2.txt", "dhl3.txt"]
counter = 0
sentiment = []
value = 0
n=0
# ngword = 0
# pword = 0
# tword=0
for i in article_arr:

    with open(i, 'r', encoding='utf-8') as f:
        wrd = []
        f_contents = f.readlines()
        for i in f_contents:
            i = i.lower()
            i = i.split(" ")
            for j in i:
                wrd.append(j)

        wrd = eliminate_except_letters_number(wrd)
        wrd = eliminate_stop_word(wrd)
        wrd = word_list_frequency(wrd)
        positive = count_positive_percentage(wrd)
        negative = count_negative_percentage(wrd)
        wrd_keys, wrd_values = wrd.keys(), wrd.values()
        wrd_keys = list(wrd_keys)
        wrd_values = list(wrd_values)
        print(positive-negative)
        value += (positive-negative)

        # ngword += count_negative(wrd)
        # pword += count_positive(wrd)
        # tword += allword(wrd)
        counter += 1
        # print(value)
        if counter == 3:
            value = (round(value/3, 2))
            # snt = round(((pword-ngword)/tword),2)
            sentiment.append(value)
            counter = 0
            print(sentiment)
            value=0
            # ngword = 0
            # pword = 0
            # tword=0

        # fig = go.Figure([go.Bar(x=wrd_keys, y=wrd_values)])
        # fig.write_html(f'{n}value.html', auto_open=True)
        # fig = go.Figure([go.Bar(x=["Positive", "Negative"], y=[positive, negative])])
        # fig.write_html(f'{n}percent.html', auto_open=True)
        # n+=1
