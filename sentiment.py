import pandas as pd
from afinn import Afinn
import re

a= Afinn()

df=pd.read_csv(r"C:\Users\nisht\Downloads\hotel_reviews.csv")
df=df[['Name','Review_Text']]
df=df.dropna()
print(df)

def only_words(review):
    return ' '.join(re.findall(r'\b\w+\b', review))

df['Review_Text'] = df['Review_Text'].apply(only_words)

def sentiment_calculator(review):
    return a.score(review)

df['sentiment score'] =df['Review_Text'].apply(sentiment_calculator)
print(df)

df.to_csv('sentiment analysis.csv',index=False)
df = pd.read_csv('sentiment analysis.csv')
df.groupby('Name').agg(
    avg = ('sentiment score','mean')
)

# to get values on order
df=df.sort_values('avg', ascending=False)
print(df)


