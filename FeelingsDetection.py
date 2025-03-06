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

if __name__ == "__main__":
    analyze_sentiments('/Users/achrafbenamer/Desktop/METROLOGIE TP 1/logs.txt')