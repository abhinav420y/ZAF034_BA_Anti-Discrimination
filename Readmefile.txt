Anti Discrimination Project
Project Overview
The Anti Discrimination Project is designed to analyze staff interactions with airline passengers to detect potential discriminatory behavior. By monitoring body language, tone of voice, and facial expressions, this project aims to identify patterns of discrimination and alert management for corrective action. By doing so, we can promote a more inclusive environment and improve the overall passenger experience.

Data
The dataset used for this project is the "Tweets.csv" dataset, which contains tweets about various airlines. The dataset consists of 14,640 rows and 15 columns, with each row representing a single tweet.

Original Files:
ZAF034_BA_Anti-Discrimination - https://colab.research.google.com/drive/1-fzAc5ONRuYQ2fWeB1roqP1tlZIetewD?usp=sharing
Load_predict file - https://colab.research.google.com/drive/1S9Dn38ZAsUCRXjFctvYHVnCKBtWKstNi?usp=sharing

Libraries Used
Pandas
Numpy
Seaborn
Matplotlib
Pickle
NLTK
Keras
Tensorflow

Data Cleaning
Irrelevant columns such as 'tweet_id', 'airline_sentiment_confidence', 'negativereason_confidence', 'airline', 'name', 'tweet_created', 'retweet_count', and 'user_timezone' were removed from the dataset.
The 'airline_sentiment' column was converted to numerical values with 'negative' as -1, 'neutral' as 0, and 'positive' as 1.
The 'text' column was cleaned by removing URLs, mentions, emojis, non-letter characters, and stop words.
Exploratory Data Analysis
The most common negative review reasons were identified and visualized through bar charts.
The distribution of airline sentiments was visualized through countplots for each airline.
Modeling
The cleaned data was preprocessed by tokenizing and padding sequences. A sequential model was then trained using the preprocessed data to classify tweets as negative, neutral, or positive. The model achieved an accuracy of 81.75% on the test set.

Conclusion
Through the Anti Discrimination Project, we were able to identify patterns of discriminatory behavior and provide insights to airlines for corrective action. By promoting a more inclusive environment, we can improve the overall passenger experience and foster a more positive relationship between airlines and their customers
