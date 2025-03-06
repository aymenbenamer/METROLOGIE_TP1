import pandas as pd
import re  # Pour utiliser les expressions régulières afin d'extraire les nombres
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()

import pandas as pd

file_path = "/Users/achrafbenamer/Desktop/METROLOGIE TP 1/logs.txt"
csv_output_path = "/Users/achrafbenamer/Desktop/METROLOGIE TP 1/output.csv"

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

# Convertir la liste de sentiments en DataFrame
sentiment_df = pd.DataFrame(sentiments)

# Concaténer les scores de sentiment avec le DataFrame original
df = pd.concat([df, sentiment_df], axis=1)


# Affichage des premières lignes pour vérifier si les colonnes sont correctement définies
print(df.head())

# Sauvegarder le DataFrame dans un fichier CSV avec un séparateur ';'
df.to_csv(csv_output_path, index=False, encoding="utf-8", sep=";")

# Afficher le DataFrame final
print(df.to_string(index=False))

