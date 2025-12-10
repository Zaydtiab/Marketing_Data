import csv
import requests
import os
import time
from dotenv import load_dotenv # Import du gestionnaire de variables d'environnement

# 1. Chargement des variables secrètes depuis le fichier .env
load_dotenv()

# 2. Récupération de la clé et de l'email
API_KEY = os.getenv("BREVO_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL") 
URL = "https://api.brevo.com/v3/smtp/email"

def send_email_via_api(email, prenom):
    # Vérification que la clé est bien chargée
    if not API_KEY:
        print("ERREUR : Clé API non trouvée dans le fichier .env")
        return 0

    headers = {
        'accept': 'application/json',
        'api-key': API_KEY,
        'content-type': 'application/json'
    }
    
    # Construction de l'email
    payload = {
        "sender": {"name": "Mon Projet TP", "email": SENDER_EMAIL},
        "to": [{"email": email, "name": prenom}],
        "subject": f"Bienvenue {prenom} !",
        "htmlContent": f"<html><body><h1>Bonjour {prenom},</h1><p>Ceci est un test technique réel depuis mon script Python.</p></body></html>"
    }

    try:
        # Envoi réel via l'API
        response = requests.post(URL, json=payload, headers=headers)
        
        # Si le code est 201, c'est réussi
        if response.status_code == 201:
            return 201
        else:
            print(f"Erreur API ({response.status_code}): {response.text}")
            return response.status_code
    except Exception as e:
        print(f"Erreur de connexion : {e}")
        return 500

def main():
    print("--- Démarrage de l'envoi réel ---")
    
    # On utilise un fichier CSV de test pour ne pas spammer tout le monde
    # Pour le test, vous pouvez créer un fichier 'test_list.csv' avec juste VOTRE email
    csv_file = 'inscrits.csv' 
    
    if not os.path.exists(csv_file):
        print(f"Fichier {csv_file} introuvable.")
        return

    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            email = row['email']
            prenom = row['prenom']
            
            print(f"Envoi en cours à {email}...")
            status = send_email_via_api(email, prenom)
            
            if status == 201:
                print(f"[SUCCÈS] Email envoyé !")
            else:
                print(f"[ÉCHEC] L'envoi a échoué.")
            
            time.sleep(1) # Pause d'une seconde entre chaque envoi

if __name__ == "__main__":
    main()