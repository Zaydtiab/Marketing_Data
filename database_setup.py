import sqlite3
import random
from datetime import datetime
from faker import Faker

# Configuration
fake = Faker('fr_FR') 
DB_NAME = "marketing.db"

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    print("--- 1. Architecture de la base de données ---")

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sessions (
        session_id VARCHAR(50) PRIMARY KEY,
        user_id VARCHAR(50),
        ip_address VARCHAR(20),
        country VARCHAR(50),
        start_time TEXT,
        pages_viewed INT,
        converted BOOLEAN,
        channel VARCHAR(50)
    )
    ''')

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
    print("Tables créées.")

def generate_pro_data(n=2000):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Nettoyage
    cursor.execute("DELETE FROM sessions")
    cursor.execute("DELETE FROM events")
    
    print(f"--- 2. Génération de {n} logs (Logique RENFORCÉE pour ML) ---")
    
    channels = ['organic', 'paid', 'email', 'social']
    
    for _ in range(n):
        # --- PARTIE FAKER ---
        user_uuid = fake.uuid4()[:8]
        ip = fake.ipv4()
        country = fake.country()
        session_id = f"sess_{fake.uuid4()}"
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # --- PARTIE LOGIQUE RENFORCÉE ---
        # On force des profils très typés
        
        # 1. Choix du profil
        profil_type = random.choices(['touriste', 'client_serieux'], weights=[70, 30], k=1)[0]
        
        if profil_type == 'client_serieux':
            # Le client sérieux vient par Email ou Organic, regarde beaucoup de pages
            channel = random.choice(['email', 'organic'])
            pages = random.randint(10, 25) # Beaucoup de pages
            converted = 1 # Il achète presque tout le temps
            
            # Petite part d'aléatoire (10% de chance qu'il n'achète pas quand même)
            if random.random() < 0.1: converted = 0

        else: # C'est un 'touriste'
            # Le touriste vient des réseaux sociaux, regarde peu de pages
            channel = random.choice(['social', 'paid'])
            pages = random.randint(1, 8) # Peu de pages
            converted = 0 # Il n'achète presque jamais
            
            # Petite part d'aléatoire (5% de chance qu'il achète sur un coup de tête)
            if random.random() < 0.05: converted = 1
        
        # Insertion SESSIONS
        cursor.execute('''
            INSERT INTO sessions (session_id, user_id, ip_address, country, start_time, pages_viewed, converted, channel)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (session_id, user_uuid, ip, country, current_time, pages, converted, channel))
        
        # Insertion EVENTS
        if converted:
            base_rev = random.randint(30, 100)
            revenue = base_rev + (pages * 2)
            cursor.execute('''
                INSERT INTO events (user_id, event_type, revenue, channel)
                VALUES (?, 'purchase', ?, ?)
            ''', (user_uuid, revenue, channel))
            
    conn.commit()
    conn.close()
    print(f"✅ Terminé ! {n} lignes avec des profils très marqués (Facile pour l'IA).")

if __name__ == "__main__":
    create_tables()
    generate_pro_data(n=2000)