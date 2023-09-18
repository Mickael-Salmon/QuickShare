
# Quick File and Web App Sharing with ngrok

## 📖 Introduction

Ce README vous guide à travers la mise en place d'un partage de fichiers ou d'une application web de manière temporaire en utilisant Python et ngrok.

## 📝 Prérequis
Python 3.x
ngrok
Un compte ngrok (pour obtenir un token d'authentification)
virtualenv pour la gestion des environnements virtuels Python

## 🐟 Pour les utilisateurs de Fish Shell

1. Activez l'environnement virtuel Python :

    ```fish
    source venv/bin/activate.fish
    ```

2. Installez les packages Python requis :

    ```fish
    pip install colorama tqdm requests
    ```

## 🐚 Pour les utilisateurs de Bash ou Zsh

1. Activez l'environnement virtuel Python :

    ```bash
    source venv/bin/activate
    ```

2. Installez les packages Python requis :

    ```bash
    pip install colorama tqdm requests
    ```

## 🚀 Utilisation

1. **Partage de fichiers**

    Exécutez le script Python pour démarrer un serveur HTTP sur le port de votre choix (par exemple 8080).

    ```bash
    python temporary_file_sharing_with_ngrok_v3.py
    ```

    Suivez les instructions à l'écran pour partager vos fichiers.

2. **Partage d'application web**

    Assurez-vous que votre application web est en cours d'exécution sur le port de votre choix (par exemple 3000).

    ```bash
    python temporary_file_sharing_with_ngrok_v3.py
    ```

    Suivez les instructions à l'écran pour partager votre application web.

## 🛑 Arrêt

Appuyez sur [Enter] ou Ctrl+C pour arrêter le serveur et ngrok.

## 📜 License

Ce projet est sous licence MIT.

---

Happy sharing! 😊
