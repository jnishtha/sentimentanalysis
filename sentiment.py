import pandas as pd
from afinn import Afinn
import re
# Initialize afinn sentiment analyzer
a= Afinn()

# Load Dataset
df=pd.read_csv(r"C:\Users\nisht\Downloads\hotel_reviews.csv")

# Select relevant columns and drop NaN values
df=df[['Name','Review_Text']]
df=df.dropna()

# Function to clean review text
def only_words(review):
    return ' '.join(re.findall(r'\b\w+\b', review))

# Apply text cleaning
df['Review_Text'] = df['Review_Text'].apply(only_words)

# Function to get sentiment score
def sentiment_calculator(review):
    return a.score(review)

# Applysentiment analysis
df['sentiment score'] =df['Review_Text'].apply(sentiment_calculator)

# save processed data
df.to_csv('sentiment analysis.csv',index=False)

df = pd.read_csv('sentiment analysis.csv')


# Group by 'Name' and calculate average sentiment score
df_grouped =df.groupby('Name',as_index=False).agg(
    avg = ('sentiment score','mean')
)

# 
# Group by 'Name' and calculate average sentiment score
df=df_grouped.sort_values('avg', ascending=False).reset_index(drop=True)
print(df_grouped)

