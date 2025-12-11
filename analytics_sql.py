import sqlite3
import pandas as pd

# Connexion à la base créée à l'étape 1
conn = sqlite3.connect("marketing.db")

print("=== RAPPORT ANALYTIQUE (KPIs) ===")

# KPI 1 : Taux de conversion par canal 
print("\n--- 1. Taux de conversion par Canal ---")
query_conversion = '''
SELECT 
    channel, 
    COUNT(*) as total_sessions,
    SUM(converted) as total_ventes,
    ROUND(CAST(SUM(converted) AS FLOAT) / COUNT(*) * 100, 2) as taux_conversion
FROM sessions 
GROUP BY channel
ORDER BY taux_conversion DESC;
'''
df_conv = pd.read_sql_query(query_conversion, conn)
print(df_conv)

# KPI 2 : Revenu Moyen par Utilisateur (ARPU) 
print("\n--- 2. Revenu Moyen (ARPU) ---")
query_arpu = '''
SELECT 
    ROUND(AVG(revenue), 2) as revenu_moyen_panier
FROM events
WHERE event_type = 'purchase';
'''
df_arpu = pd.read_sql_query(query_arpu, conn)
print(df_arpu)

conn.close()