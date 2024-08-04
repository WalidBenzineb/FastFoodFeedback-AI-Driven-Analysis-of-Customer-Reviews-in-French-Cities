import pandas as pd
import torch
from transformers import CamembertTokenizer, CamembertForSequenceClassification
from torch.utils.data import DataLoader, TensorDataset
import os
from tqdm import tqdm
import warnings

# Vérifier si CUDA est disponible
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Utilisation du dispositif : {device}")

def load_model():
    tokenizer = CamembertTokenizer.from_pretrained("camembert-base")
    model = CamembertForSequenceClassification.from_pretrained("camembert-base", num_labels=5)
    model.to(device)
    return tokenizer, model

def predict_sentiment(model, tokenizer, texts, batch_size=32):
    model.eval()
    all_scores = []

    # Filtrer les textes non valides
    valid_texts = [str(text) for text in texts if pd.notna(text)]

    dataset = tokenizer(valid_texts, truncation=True, padding=True, max_length=512, return_tensors="pt")
    dataset = TensorDataset(dataset['input_ids'], dataset['attention_mask'])
    dataloader = DataLoader(dataset, batch_size=batch_size)

    with torch.no_grad():
        for batch in tqdm(dataloader, desc="Notation des avis"):
            input_ids, attention_mask = [b.to(device) for b in batch]
            outputs = model(input_ids, attention_mask=attention_mask)
            scores = torch.nn.functional.softmax(outputs.logits, dim=-1)
            all_scores.extend(scores.cpu().numpy())

    # Convertir les scores en notes de 1 à 5
    return [score.argmax() + 1 for score in all_scores]

def score_reviews(input_dir, output_dir):
    warnings.warn("Ce modèle n'a pas été affiné pour la tâche spécifique de notation des avis de restaurants. Les résultats peuvent ne pas être optimaux.", UserWarning)

    tokenizer, model = load_model()

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.startswith('cleaned_') and filename.endswith('.csv'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"scored_{filename}")

            df = pd.read_csv(input_path)
            
            # Vérifier si la colonne 'cleaned_review' existe
            if 'cleaned_review' not in df.columns:
                print(f"Erreur : La colonne 'cleaned_review' n'existe pas dans {filename}")
                continue

            scores = predict_sentiment(model, tokenizer, df['cleaned_review'].tolist())

            # S'assurer que le nombre de scores correspond au nombre de lignes
            if len(scores) != len(df):
                print(f"Attention : {len(df) - len(scores)} avis ont été ignorés en raison de valeurs non valides.")
                # Ajouter des valeurs NaN pour les lignes ignorées
                scores = scores + [float('nan')] * (len(df) - len(scores))

            df['score'] = scores
            df.to_csv(output_path, index=False)
            print(f"Avis notés sauvegardés dans {output_path}")

if __name__ == "__main__":
    input_directory = "cleaned_reviews"
    output_directory = "scored_reviews"
    score_reviews(input_directory, output_directory)