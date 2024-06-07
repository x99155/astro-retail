Description
========

Ce projet a été généré en utilisant la CLI astro.

Astro est une solution cloud qui vous aide à vous concentrer sur vos pipelines de données et à passer moins de temps à gérer Apache Airflow, avec des fonctionnalités vous permettant de créer, d'exécuter et d'observer des données en un seul endroit.

Pour plus d'informations consultez la docs [ici](https://docs.astronomer.io/learn/get-started-with-airflow)

Pré-requis
- CLI Astro
- Docker
- IDE
- Compte Google Cloud Platform


Description du projet
================

Nous créons un DAG qui exécute les étapes nécessaires pour transférer un fichier CSV local vers BigQuery en utilisant Google Cloud Storage comme intermédiaire.

1. Import des bibliothèques et configuration du DAG :

- Importation des opérateurs nécessaires.
- Définition des paramètres par défaut du DAG et des chemins/noms utilisés dans les tâches.

2. Définition des tâches :

upload_csv_to_gcp : Transfère le fichier CSV local vers le bucket GCS spécifié.
create_retail_dataset : Crée un dataset vide dans BigQuery.
gcs_to_bigquery : Importe le fichier CSV de GCS vers une table BigQuery.

3. Définition de l'ordre des tâches :

- Les tâches sont organisées dans l'ordre correct en utilisant l'opérateur >>


Utilisation
===========================

1. Générez un nouveau projet avec la commande `astro dev init`

2. Démarrez airflow sur votre machine local avec la commande `astro dev start`

Cette commande fera tourner 4 conteneurs Docker sur votre machine, chacun pour un composant Airflow différent :

- Postgres : base de données de métadonnées d'Airflow
- Serveur Web : le composant Airflow responsable du rendu de l'interface utilisateur Airflow
- Scheduler : Le composant Airflow chargé de surveiller et de déclencher les tâches
- Triggerer : Le composant Airflow chargé de déclencher les tâches différées

Vérifiez que les 4 conteneurs Docker ont été créés en exécutant `docker ps`.

NB: L'exécution de `astro dev start` démarrera votre projet avec le serveur Web Airflow exposé sur le port 8080 et Postgres exposé sur le port 5432. Si l'un de ces ports est déjà alloué, vous pouvez [soit arreter les conteneurs existants, soit changer de port](https://docs.astronomer.io/astro/test-and-troubleshoot-locally#ports-are-not-available).

Accédez à l'interface utilisateur Airflow pour votre projet Airflow local. Pour ce faire, allez sur http://localhost:8080/ et connectez-vous avec « admin » pour votre nom d'utilisateur et votre mot de passe.

