from fastapi import FastAPI
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator

app=FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'Sudhanshu'}}

@app.get('/about')
def about():
    return {'data':{'about page'}}

@app.get('/{sentence}')
def sentiment_scores(sentence):
    translated_text = GoogleTranslator(source='auto', target='en').translate(sentence)
    sid_obj = SentimentIntensityAnalyzer()
    print(translated_text)
    sentiment_dict = sid_obj.polarity_scores(translated_text)
     
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
 
    print("Sentence Overall Rated As", end = " ")
    if sentiment_dict['compound'] >= 0.05 :
        return{'data':{'Positive'}}
 
    elif sentiment_dict['compound'] <= - 0.05 :
         return{'data':{'Negitive'}}
 
    else :
         return{'data':{'Neutral'}}
 