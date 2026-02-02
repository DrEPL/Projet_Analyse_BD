#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de génération de données synthétiques pour l'exercice de segmentation client.
Génère 1000 clients avec Age, RevenuAnnuel (en milliers de $), et ScoreDepense (1-100).
"""

import pandas as pd
import numpy as np
import os

# Configuration de la graine aléatoire pour la reproductibilité
np.random.seed(42)

# Nombre de clients
n_clients = 1000

# Génération des données
data = {
    "CustomerID": range(1, n_clients + 1),
    "Age": np.random.randint(18, 70, size=n_clients),
    "RevenuAnnuel": np.random.randint(15, 140, size=n_clients),  # en milliers de dollars
    "ScoreDepense": np.random.randint(1, 100, size=n_clients)    # score de 1 à 100
}

# Création du DataFrame
df = pd.DataFrame(data)

# Sauvegarde en CSV
# output_file = "/home/ubuntu/clients.csv"
# Répertoire de base = dossier où se trouve ce script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Chemin vers le dossier data (frère du dossier app)
output_file = os.path.join(BASE_DIR, "..", "data", "clients.csv")
print(output_file)
df.to_csv(output_file, index=False)

print(f"✓ Fichier généré : {output_file}")
print(f"✓ Nombre de clients : {len(df)}")
print(f"\nAperçu des données :")
print(df.head(10))
print(f"\nStatistiques descriptives :")
print(df.describe())
