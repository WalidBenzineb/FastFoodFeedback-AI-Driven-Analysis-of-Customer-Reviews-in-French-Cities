import pandas as pd
import re
import os
from unidecode import unidecode
import torch
from tqdm import tqdm

# Vérifier si CUDA est disponible
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Utilisation du dispositif : {device}")

def clean_text(text):
    # Convertir en minuscules
    text = text.lower()
    # Supprimer les accents
    text = unidecode(text)
    # Supprimer les URLs
    text = re.sub(r'http\S+', '', text)
    # Supprimer les caractères spéciaux et les chiffres
    text = re.sub(r'[^a-z\s]', '', text)
    # Supprimer les espaces supplémentaires
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_data(input_dir, output_dir):
    # Créer le répertoire de sortie s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)

    # Traiter chaque fichier dans le répertoire d'entrée
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"cleaned_{filename}")

            # Lire le fichier CSV
            df = pd.read_csv(input_path)

            # Vérifier si les colonnes 'date' et 'review' existent
            if 'date' not in df.columns or 'review' not in df.columns:
                print(f"Erreur : Les colonnes 'date' et 'review' sont requises dans {filename}")
                print(f"Colonnes disponibles : {df.columns.tolist()}")
                continue

            # Nettoyer la colonne 'review'
            tqdm.pandas(desc=f"Nettoyage des avis dans {filename}")
            df['cleaned_review'] = df['review'].progress_apply(clean_text)

            # Sauvegarder les données nettoyées
            df.to_csv(output_path, index=False)
            print(f"Données nettoyées sauvegardées dans {output_path}")

if __name__ == "__main__":
    input_directory = "reviews"
    output_directory = "cleaned_reviews"
    clean_data(input_directory, output_directory)