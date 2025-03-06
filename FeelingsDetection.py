import pandas as pd
import re  # Pour utiliser les expressions régulières afin d'extraire les nombres
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


def lire_dataframe(file_path, csv_output_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lignes = [ligne.strip() for ligne in file.readlines()]

        # Séparation des colonnes Date et Contenu, et extraction des nombres
        data = []
        for ligne in lignes:
            # Séparer la ligne en Date et Contenu
            parts = ligne.split("\t", 1) if "\t" in ligne else [ligne, ""]
            
            # Extraire le nombre à la fin de la ligne (si présent)
            match = re.search(r'(\d+)$', parts[1])  # Recherche d'un nombre à la fin de la ligne
            nombre = match.group(1) if match else ""  # Si un nombre est trouvé, on le prend, sinon on laisse vide
            
            # Ajouter le nombre à la ligne
            data.append([parts[0], parts[1], nombre])

        # Création du DataFrame avec colonnes Date, Contenu, Nombre
        df = pd.DataFrame(data, columns=["Date", "Contenu", "Nombre"])

        # Améliorer l'affichage
        pd.set_option('display.colheader_justify', 'center')

        # Enregistrer le DataFrame dans un fichier CSV
        df.to_csv(csv_output_path, index=False, encoding="utf-8")

        return df
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None

# Exemple d'utilisation
file_path = "/Users/achrafbenamer/Desktop/METROLOGIE TP 1/logs.txt"
csv_output_path = "/Users/achrafbenamer/Desktop/METROLOGIE TP 1/csv_output.txt"

df = lire_dataframe(file_path, csv_output_path)






analyze_sentiments('/Users/achrafbenamer/Desktop/METROLOGIE TP 1/logs.txt')
