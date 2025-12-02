# 🏅 Analyse des Données des Jeux Olympiques (1896 - 2016)

## 📝 Description du Projet

Ce projet vise à explorer et à analyser un ensemble de données historiques des Jeux Olympiques, couvrant la période de **1896 à 2016**. L'objectif est d'identifier des **modèles, des tendances** et des **évolutions** au fil du temps dans le cadre du plus important événement sportif mondial.

L'analyse se concentre sur :
* L'évolution des caractéristiques physiques (taille, poids, âge) des athlètes.
* Les tendances de participation des pays et des athlètes féminines/masculins.
* L'étude spécifique des performances de certains pays ou sports (e.g., Tunisie, Gymnastique).

***

## ⚙️ Structure du Projet

Le dépôt est organisé de la manière suivante :

| Fichier/Dossier | Description |
| :--- | :--- |
| `athletes.xlsx - athletes.csv` | Le jeu de données principal contenant les informations sur les athlètes, les événements et les médailles (fichier CSV converti). |
| `noc_regions.csv` | Fichier de données de support pour lier les codes NOC (Comités Nationaux Olympiques) à leurs régions correspondantes. |
| `Project olympic games analysis.py` | Le script Python principal contenant le code pour le nettoyage des données, la fusion, l'analyse et la génération des visualisations. |
| `README.md` | Ce document. |

***

## 📊 Sources des Données

Ce projet utilise deux jeux de données majeurs :

1.  **`athletes.xlsx - athletes.csv`** : Contient des enregistrements détaillés de tous les athlètes et événements olympiques de 1896 à 2016.
2.  **`noc_regions.csv`** : Fichier de référence utilisé pour joindre les codes NOC aux noms de pays ou de régions lisibles.

***

## 🚀 Configuration et Exécution

Pour exécuter l'analyse sur votre machine locale, suivez ces étapes.

### Prérequis

Assurez-vous d'avoir **Python** installé (version 3.x recommandée) ainsi que les bibliothèques suivantes :

```bash
pip install pandas numpy matplotlib seaborn
