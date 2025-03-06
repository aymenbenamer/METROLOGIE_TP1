"""from transformers import pipeline

def analyze_sentiments(file_path):
    
    sentiment_analyzer = pipeline("sentiment-analysis", model="camembert-base")
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        sentiment = sentiment_analyzer(line)
        print(sentiment)


analyze_sentiments('/Users/achrafbenamer/Desktop/METROLOGIE TP 1/logs.txt')"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiments(file_path):
    analyzer = SentimentIntensityAnalyzer()
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        sentiment = analyzer.polarity_scores(line)
        print(f"Sentence: {line.strip()}")
        print(f"Sentiment: {sentiment}")
        print("-" * 50)


analyze_sentiments('/Users/achrafbenamer/Desktop/METROLOGIE TP 1/logs.txt')
