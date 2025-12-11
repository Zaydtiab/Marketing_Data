import sqlite3
import random
from datetime import datetime

# Nom de la base de données
DB_NAME = "marketing.db"

def create_tables():
    """
    Crée l'architecture (Schema) demandée dans le PDF[cite: 72, 84].
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    print("--- 1. Création des tables SQL ---")

    # Table SESSIONS (Visites)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sessions (
        session_id VARCHAR(50) PRIMARY KEY,
        user_id VARCHAR(50),
        start_time TIMESTAMP,
        pages_viewed INT,
        converted BOOLEAN,
        channel VARCHAR(50)
    )
    ''')

    # Table EVENTS (Achats)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS events (
        event_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id VARCHAR(50),
        event_type VARCHAR(50),
        revenue DECIMAL(10,2),
        channel VARCHAR(50)
    )
    ''')
    conn.commit()
    print("Tables 'sessions' et 'events' prêtes.")

def generate_fake_data(n=200):
    """
    Simule des données pour remplir la base (ETL).
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    print(f"--- 2. Génération de {n} visites simulées ---")
    
    channels = ['organic', 'paid', 'email', 'social']
    
    for i in range(n):
        user_id = f"user_{i}"
        session_id = f"sess_{random.randint(10000,99999)}"
        channel = random.choice(channels)
        pages = random.randint(1, 12)
        
        # 20% de chance d'acheter
        converted = 1 if random.random() < 0.2 else 0 
        
        # Insertion dans SESSIONS
        cursor.execute('''
            INSERT INTO sessions VALUES (?, ?, ?, ?, ?, ?)
        ''', (session_id, user_id, datetime.now(), pages, converted, channel))
        
        # Si achat, insertion dans EVENTS
        if converted:
            revenue = random.randint(20, 200)
            cursor.execute('''
                INSERT INTO events (user_id, event_type, revenue, channel)
                VALUES (?, 'purchase', ?, ?)
            ''', (user_id, revenue, channel))
            
    conn.commit()
    conn.close()
    print("Données insérées avec succès dans marketing.db !")

if __name__ == "__main__":
    create_tables()
    generate_fake_data()