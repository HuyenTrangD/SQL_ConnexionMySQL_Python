# Connexion avec MySQL via Python

Ce notebook donne des instructions pour connecter à la base de données dans un serveur MySQL via Python.

## Installation
- Créer un environnement virtuel
    ```bash
    # Linux
    python -m venv .venv
    # Windows
    py -m venv .venv
    ```
- Activer l'environnement virtuel
    ```bash
    # Linux
    .venv/bin/activate
    # Windows (batch/cmd)
    .venv/Scripts/activate.bat
    # Windows (powershell)
    .venv/Scripts/Activate.ps1
    ```
- Installer les dépendances
    ```bash
    pip install -r requirements.txt
    ```

- Installer my-sql-connector-python
    ```bash
    pip install my-sql-connector-python
    ```
- Installer pyodbc & choisir le serveur correspondant
    ```bash
    pip install pyodbc
    ```
'MySQL ODBC 8.0 ANSI Driver'

'MySQL ODBC 8.0 Unicode Driver'

'MariaDB ODBC 3.1 Driver'
