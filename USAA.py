# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:56:09 2020

@author: allyt
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import operator
pd.set_option("display.max_colwidth", 200)

#from sklearn.datasets import fetch_20newsgroups
#
#dataset = fetch_20newsgroups(shuffle=True, random_state=1, remove=('headers', 'footers', 'quotes'))
#documents = dataset.data
#len(documents)
dataset = pd.read_csv(r'C:\Users\allyt\Documents\Spring2020\CIS450\cis450-rta-master\cis450-rta-master\tweetset.csv', encoding='latin1',sep= ",")

data = dataset.Tweets
twitter_df = pd.DataFrame({'document':data})

# removing everything except alphabets`twitter_df['clean_doc'] = news_df['document'].str.replace("[^a-zA-Z#]", " ")
twitter_df['clean_doc'] = twitter_df['document'].str.replace("[^a-zA-Z#]", " ")
# removing short words
twitter_df['clean_doc'] = twitter_df['clean_doc'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))

# make all text lowercase
twitter_df['clean_doc'] = twitter_df['clean_doc'].apply(lambda x: x.lower())

from nltk.corpus import stopwords
stop_words = stopwords.words('english')

# tokenization
tokenized_doc = twitter_df['clean_doc'].apply(lambda x: x.split())

# remove stop-words
tokenized_doc = tokenized_doc.apply(lambda x: [item for item in x if item not in stop_words])
numtweet = len(tokenized_doc)
# de-tokenization
detokenized_doc = []
for i in range(len(twitter_df)):
    t = ' '.join(tokenized_doc[i])
    detokenized_doc.append(t)

twitter_df['clean_doc'] = detokenized_doc

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words=['english'], 
max_features= 1000, # keep top 1000 terms 
max_df = 0.5, 
smooth_idf=True)

X = vectorizer.fit_transform(twitter_df['clean_doc'])

X.shape # check shape of the document-term matrix

from sklearn.decomposition import TruncatedSVD

# SVD represent documents and terms in vectors 
svd_model = TruncatedSVD(n_components=5, algorithm='randomized', n_iter=100, random_state=122)

svd_model.fit(X)

len(svd_model.components_)

terms = vectorizer.get_feature_names()

for i, comp in enumerate(svd_model.components_):
    terms_comp = zip(terms, comp)
    sorted_terms = sorted(terms_comp, key= lambda x:x[1], reverse=True)[:5]
    print("Topic "+str(i)+": ")
    for t in sorted_terms:
        print(t[0])
        print(" ")
        
    topic=[]
    for i in sorted_terms:
        topic.append(i[0])
        
    simlist = []
    
    for j in range(numtweet):
        Tweetvec = tokenized_doc[j]
        sim = 0
        if topic[0] in Tweetvec:
                sim+=1    
        if topic[1] in Tweetvec:
                sim+=.75
        if topic[2] in Tweetvec:
                sim+=.50
        if topic[3] in Tweetvec:
                sim+=.25
        if topic[4] in Tweetvec:
                sim+=.1  
        vecsim=(j,sim)
        simlist.append(vecsim)
        
    simlist.sort(key=operator.itemgetter(1), reverse =1)
    
    print('Top 3 tweets')
    for t in range(3):     
        tweet=simlist[t][0]
        print()
        print(data[tweet])
            
            
        
