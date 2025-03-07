import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import threading
import time


analyzer = SentimentIntensityAnalyzer()


file_path = "/Users/achrafbenamer/Desktop/METROLOGIE TP 1/logs.txt"
csv_output_path = "/Users/achrafbenamer/Desktop/METROLOGIE TP 1/output.csv"

def run_script():
    while True:
        # Lire le fichier texte avec des tabulations comme séparateurs sans entêtes, en définissant les noms des colonnes 
        df = pd.read_csv(file_path, sep='\t', encoding="utf-8", header=None, names=["Date", "Contenu", "Nombre"])

        # Convertir la colonne 'Date' en format datetime avec un format spécifique (YYYYMMDD HH:MM:SS)
        df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d %H:%M:%S', errors='coerce')

        # Extraire l'année, le mois, le jour, et le temps de la colonne 'Date'
        df['Annee'] = df['Date'].dt.year
        df['Mois'] = df['Date'].dt.month
        df['Jour'] = df['Date'].dt.day
        df['Time'] = df['Date'].dt.strftime('%H:%M:%S')  # Extraire l'heure, les minutes et les secondes

        # Initialiser une liste pour stocker les scores de sentiment
        sentiments = []

        # Parcourir chaque ligne de la colonne 'Contenu'
        for line in df.Contenu:
            sentiment = analyzer.polarity_scores(line)
            sentiments.append(sentiment)
            print(f"Sentence: {line.strip()}")
            print(f"Sentiment: {sentiment}")
            print("-" * 50)
        
        print(sentiments)
        # Convertir la liste de sentiments en DataFrame
        sentiment_df = pd.DataFrame(sentiments)

        print(df.head())

        for index, cpd in sentiment_df.iterrows():
            if df.at[index, "Nombre"] < 40:
                sentiment_df.at[index, "compound"] += cpd["compound"]*0.05
            elif df.at[index, "Nombre"] > 60:
                sentiment_df.at[index, "compound"] -= cpd["compound"]*0.05

        # Concaténer les scores de sentiment avec le DataFrame original
        df = pd.concat([df, sentiment_df], axis=1)

        # Affichage des premières lignes pour vérifier si les colonnes sont correctement définies
        print(df.head())

        # Sauvegarder le DataFrame en CSV
        df.to_csv(csv_output_path, index=False)

        # Attendre 15 secondes avant la prochaine exécution
        time.sleep(10)

# Créer et démarrer le thread
thread = threading.Thread(target=run_script)
thread.start()
