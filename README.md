# 📈 Marketing Automation & Data Analytics Pipeline

Ce projet a été réalisé dans le cadre du module **Web Marketing & CRM** (ENSAH). Il simule le cycle de vie complet de la donnée marketing : de l'acquisition client à la prédiction des ventes par Intelligence Artificielle.

## 🚀 Fonctionnalités Clés

Le projet est divisé en 3 blocs techniques indépendants :

### 1. Acquisition & Automatisation (Emailing)
- **Objectif :** Automatisation de l'envoi d'emails de bienvenue.
- **Tech :** Python, API REST (Brevo/Sendinblue).
- **Sécurité :** Gestion des clés API via variables d'environnement (`.env`).

### 2. Engagement (Social Media Analytics)
- **Objectif :** Analyser la performance des posts (Facebook, Instagram, LinkedIn).
- **Tech :** Pandas, Seaborn, Matplotlib.
- **Insights :** Calcul du Taux d'Engagement et identification des meilleures heures de publication.

### 3. Conversion & Data Engineering (SQL + ML)
- **ETL Pipeline :** Création d'un Data Warehouse SQL (SQLite) avec simulation de trafic (Tables `sessions` et `events`).
- **Analytics :** Calcul des KPIs clés (Taux de conversion par canal, ARPU) via SQL.
- **Machine Learning :** Modèle **Random Forest** pour prédire la conversion utilisateur.
  - *Performance :* Optimisation du Recall à **75%** sur la détection des acheteurs (Class Weight Balanced).

## 🛠️ Installation et Utilisation

1. **Cloner le projet**
   ```bash
   git clone [https://github.com/Zaydtiab/Marketing_Data.git](https://github.com/Zaydtiab/Marketing_Data.git)
   cd Marketing_Data