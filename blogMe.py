# -*- coding: utf-8 -*-
"""
Created on Sat May 14 15:46:12 2022

@author: Shreya
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading excel file
data = pd.read_excel('articles.xlsx')

#summary
data.describe()

#summary of columns
data.info()
#counting no. of articles per source
#format of group by: df.groupby(['column_to_group])['column_to_count'].count()

data.groupby(['source_id'])['article_id'].count()

#number of reaction by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()  # we need sum

#dropping column
data=data.drop('engagement_comment_plugin_count',axis=1)

#function
def thisIsFunc():
    print('first function')
thisIsFunc()


#function with variable
def aboutMe(name,surname,location):
    print('My name is '+name + ' ' +surname +' from '+ location)
    #return name
s = aboutMe('Shreya', 'Dhar','Patna')


#for loops in function

def favfood(food):
    for x in food:
        print('Top food is '+x)

fastfood = ['burgers','pizza','pie']
favfood(fastfood)

#lets create a for loop to isolate each title row
keyword_flag = []
keyword = 'crash'

for x in range(0,10):
    heading = data['title'][x]
    if keyword in heading:
        flag = 1
    else:
        flag = 0
    keyword_flag.append(flag)
keyword_flag


#creating function

def keywordflag(keyword):
    length = len(data)
    keyword_flag =[]
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag=0
        keyword_flag.append(flag)
    return keyword_flag

kflag = keywordflag("murder")
#creating new column in data frame
data['keyword_flag'] = pd.Series(kflag)

#sentimentIntensityAnalyzer
sent_int = SentimentIntensityAnalyzer() #initializing the class
text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

#adding a for loop to extract sentiment per title

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
length = len(data)

for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

#writing the data
data.to_excel('blogme_clean.xlsx',sheet_name='blogmedata', index=False)















