import pandas as pd
import torch
from transformers import CamembertTokenizer, CamembertForSequenceClassification
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from collections import Counter
import re
import os

# Configuration du dispositif
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Utilisation de : {device}")

# Chargement des données
input_directory = 'scored_reviews'
df_paris = pd.read_csv(os.path.join(input_directory, 'scored_cleaned_paris_reviews.csv'))
df_marseille = pd.read_csv(os.path.join(input_directory, 'scored_cleaned_marseille_reviews.csv'))
df_lyon = pd.read_csv(os.path.join(input_directory, 'scored_cleaned_lyon_reviews.csv'))

# Ajout de la colonne ville à chaque DataFrame
df_paris['ville'] = 'Paris'
df_marseille['ville'] = 'Marseille'
df_lyon['ville'] = 'Lyon'

# Combinaison des DataFrames
df = pd.concat([df_paris, df_marseille, df_lyon], ignore_index=True)
print(f"Nombre total d'avis chargés : {len(df)}")

# Préparation des données
le = LabelEncoder()
df['sentiment_score'] = df['score'].apply(lambda x: 1 if x >= 3.5 else 0)

# Fonction pour nettoyer le texte
def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = text.lower()
    return text

# Prétraitement des avis
df['avis_clean'] = df['cleaned_review'].apply(clean_text)

# Fonction pour catégoriser les avis
def categoriser_avis(texte):
    if not isinstance(texte, str):
        return {}
    categories = {
        'Food': ['nourriture', 'plat', 'menu', 'burger', 'frites', 'pizza', 'sandwich', 'salade', 'dessert', 'boisson',
                 'goût', 'saveur', 'délicieux', 'bon', 'mauvais', 'fade', 'qualité', 'frais', 'chaud', 'froid',
                 'poulet', 'boeuf', 'végétarien', 'vegan', 'portion', 'ingrédients', 'cuisine'],
        'Service': ['service', 'personnel', 'attente', 'rapide', 'lent', 'accueil', 'commande', 'serveur',
                    'serveuse', 'équipe', 'manager', 'employé', 'gentil', 'aimable', 'sympathique', 'désagréable',
                    'expérience', 'déçu', 'satisfait', 'content', 'mécontent', 'jamais', 'toujours', 'souvent'],
        'Cleanliness': ['propreté', 'sale', 'nettoyage', 'sanitaire', 'toilette', 'propre', 'hygiène', 'impeccable'],
        'Ambiance': ['décor', 'ambiance', 'bruyant', 'calme', 'confortable', 'chaleureux', 'moderne',
                     'parking', 'jeux', 'aire de jeux', 'musique', 'éclairage', 'atmosphère'],
        'Price': ['prix', 'cher', 'abordable', 'économique', 'rapport qualité-prix', 'promotion', 'réduction'],
        'Delivery': ['livraison', 'livreur', 'uber eats', 'deliveroo', 'just eat', 'à domicile', 'emporter',
                     'commande en ligne', 'application', 'retard', 'à l\'heure', 'emballage']
    }
    
    resultats = Counter()
    mots = texte.lower().split()
    for mot in mots:
        for cat, mots_cles in categories.items():
            if any(mot_cle in mot for mot_cle in mots_cles):
                resultats[cat] += 1
    
    return dict(resultats)

# Catégorisation des avis
print("Catégorisation des avis...")
df['categories'] = df['avis_clean'].apply(categoriser_avis)

# Fonction pour créer un graphique en camembert avec des couleurs fixes
def create_pie_chart(data, title, filename):
    colors = {
        'Food': '#FF9999',
        'Service': '#66B2FF',
        'Cleanliness': '#99FF99',
        'Ambiance': '#FFCC99',
        'Price': '#FF99CC',
        'Delivery': '#99CCFF'
    }
    plt.figure(figsize=(10, 6))
    plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', startangle=90, 
            colors=[colors[cat] for cat in data.keys()])
    plt.title(title)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# Création des graphiques pour chaque ville
for ville in ['Paris', 'Marseille', 'Lyon']:
    df_ville = df[df['ville'] == ville]
    
    # Avis positifs (4-5)
    avis_positifs = df_ville[df_ville['score'].isin([4, 5])]
    categories_positives = Counter([cat for cats in avis_positifs['categories'] for cat in cats])
    create_pie_chart(categories_positives, f"Breakdown of categories in positif reviews (4-5) - {ville}", f"results/categories_reviews_positifs_{ville.lower()}.png")
    
    # Avis négatifs (1-3)
    avis_negatifs = df_ville[df_ville['score'].isin([1, 2, 3])]
    categories_negatives = Counter([cat for cats in avis_negatifs['categories'] for cat in cats])
    create_pie_chart(categories_negatives, f"Breakdown of categories in negative reviews (1-3) - {ville}", f"results/categories_reviews_negatifs_{ville.lower()}.png")

print("\nAnalyse terminée. Graphiques sauvegardés.")

# Sauvegarde des résultats
df.to_csv('resultats_analyse.csv', index=False)
print("Résultats sauvegardés dans 'resultats_analyse.csv'")

# Affichage des statistiques récapitulatives pour chaque ville
for ville in ['Paris', 'Marseille', 'Lyon']:
    df_ville = df[df['ville'] == ville]
    print(f"\nRécapitulatif pour {ville}:")
    print(f"Total des avis : {len(df_ville)}")
    print(f"Avis positifs (4-5) : {len(df_ville[df_ville['score'].isin([4, 5])])}")
    print(f"Avis négatifs (1-3) : {len(df_ville[df_ville['score'].isin([1, 2, 3])])}")
    print("\nCatégories les plus mentionnées :")
    toutes_categories = Counter([cat for cats in df_ville['categories'] for cat in cats])
    print(toutes_categories.most_common(3))