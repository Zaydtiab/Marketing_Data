import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# 1. Chargement des données depuis la DB
conn = sqlite3.connect('marketing.db')
df = pd.read_sql_query("SELECT pages_viewed, channel, converted FROM sessions", conn)
conn.close()

# 2. Préparation (Encoding)
# On transforme le texte 'channel' en chiffres pour l'IA
df_clean = pd.get_dummies(df, columns=['channel'])

# 3. Définition X (indices) et y (objectif) [cite: 118]
X = df_clean.drop('converted', axis=1)
y = df_clean['converted']

# 4. Séparation Train / Test [cite: 121]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Entraînement du modèle 
print("--- Entraînement du modèle IA... ---")
model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# 6. Évaluation
y_pred = model.predict(X_test)
print(f"Précision du modèle : {accuracy_score(y_test, y_pred)*100:.2f}%")
print("\n--- Rapport détaillé ---")
print(classification_report(y_test, y_pred))