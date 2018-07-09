#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 21:54:02 2018

@author: ganeson
"""
import pandas as pd

dset = pd.read_csv('tn_gst_tweets.csv')

dset_needed = dset['text']

dset_needed.head()


import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
 
def predict(classifier,sent):
    global sid 
    scrs = sid.polarity_scores(sent)
    
    return [scrs['neg'],scrs['neu'],scrs['pos']] 

def word_feats(words):
    return dict([(word, True) for word in words])
 
negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
 
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
negcutoff = int(len(negfeats)*3/4)
poscutoff = int(len(posfeats)*3/4)
 
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
#print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats))
 
classifier = NaiveBayesClassifier.train(trainfeats)
#print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

from nltk.sentiment.vader import SentimentIntensityAnalyzer


from nltk.tokenize import word_tokenize


ops = []

for i in range(len(dset_needed)):
    one_sent = dset_needed[i]
    
    one_sent = "".join([i for i in one_sent if i not in string.punctuation])
    
    one_sent = word_tokenize(one_sent)
    
    
    from nltk.corpus import stopwords
    
    words_needed = [word for word in one_sent if word not in set(stopwords.words('english'))]
    
    from nltk.stem import PorterStemmer
    
    ps = PorterStemmer()
    
    words_needed = [ps.stem(word) for word in words_needed]
    
    out_string = " ".join(words_needed)
    
    ops.append(predict(classifier,out_string))
    
    
import numpy as np

ops_np = np.array(ops)
    
df_out = pd.DataFrame(ops_np,columns=['negative','neutral','positive'])
    
df_out.to_csv('result_latest_keerthi.csv')

    
    
    
    
    
   

