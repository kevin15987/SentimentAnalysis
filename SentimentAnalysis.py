#Importing Libraries
import pandas as pd
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Load the articles.csv file from CollectingArticles.py
df = pd.read_csv('articles.csv')

#Create a function to get the polarity (-1 <= x <= 1)
def getPolarity(text):
    return TextBlob(text).sentiment.polarity

#Creating a column for polarity
df['Polarity'] = df['Headline'].apply(getPolarity)
df.head(5)