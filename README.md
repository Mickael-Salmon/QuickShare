
# 🌐 Partage Temporaire avec Ngrok: Fichiers & Applications Web 🚀

Ce document explique comment utiliser Ngrok pour deux types de partage temporaire: le partage de fichiers et l'exposition d'applications web en développement.

C'est une approche simple et rapide pour partager des fichiers et des applications web en développement avec d'autres personnes. Cela peut être utile pour les développeurs qui souhaitent partager rapidement des fichiers ou des applications web en développement avec d'autres personnes.

## 📋 Table des matières

- [🌐 Partage Temporaire avec Ngrok: Fichiers \& Applications Web 🚀](#-partage-temporaire-avec-ngrok-fichiers--applications-web-)
  - [📋 Table des matières](#-table-des-matières)
  - [Prérequis 🛠️](#prérequis-️)
  - [Instructions sur comment préparer votre environnement virtuel Python](#instructions-sur-comment-préparer-votre-environnement-virtuel-python)
  - [Prérequis](#prérequis)
  - [Instructions](#instructions)
    - [Bash ou Zsh](#bash-ou-zsh)
    - [Fish](#fish)
  - [Après utilisation du script - Désactivation de l'environnement virtuel](#après-utilisation-du-script---désactivation-de-lenvironnement-virtuel)
  - [Installation de Ngrok 📦](#installation-de-ngrok-)
  - [Création d'un compte Ngrok 👤](#création-dun-compte-ngrok-)
  - [Partage de Fichiers avec Python 📁](#partage-de-fichiers-avec-python-)
  - [Montrer des Applications Web 💻](#montrer-des-applications-web-)
  - [Utilisation 🚀](#utilisation-)
  - [Améliorations possibles 🛠️](#améliorations-possibles-️)

---

## Prérequis 🛠️

- Python 3.x
- curl
- jq (optionnel)

## Instructions sur comment préparer votre environnement virtuel Python

pour exécuter le script de partage de fichiers. Les instructions diffèrent selon le shell que vous utilisez : bash, zsh ou fish.

## Prérequis
- Python 3.x
- pip
- virtualenv (optionnel)

## Instructions

### Bash ou Zsh
1. Ouvrez votre terminal et naviguez vers le dossier contenant le script Python.
2. Exécutez les commandes suivantes pour créer et activer un environnement virtuel :
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3. Installez les packages requis :
    ```bash
    pip install -r requirements.txt
    ```
4. Exécutez le script Python :
    ```bash
    python quickShare.py
    ```

### Fish
1. Ouvrez votre terminal et naviguez vers le dossier contenant le script Python.
2. Exécutez les commandes suivantes pour créer et activer un environnement virtuel :
    ```fish
    python -m venv venv
    source venv/bin/activate.fish
    ```
3. Installez les packages requis :
    ```fish
    pip install -r requirements.txt
    ```
4. Exécutez le script Python :
    ```fish
    python quickShare.py
    ```

## Après utilisation du script - Désactivation de l'environnement virtuel
- Pour bash ou zsh : `deactivate`
- Pour fish : `deactivate`
## Installation de Ngrok 📦

Vous pouvez installer Ngrok en suivant les instructions sur leur [site officiel](https://ngrok.com/download).

## Création d'un compte Ngrok 👤

Pour utiliser Ngrok, vous aurez besoin d'un compte. Vous pouvez vous inscrire sur leur [site web](https://ngrok.com/). Après l'inscription, récupérez votre authtoken et initialisez-le en utilisant la commande suivante :

```bash
ngrok authtoken VOTRE_TOKEN_ICI
```

---

## Partage de Fichiers avec Python 📁

Au lieu d'utiliser un script shell, nous utilisons ici un script Python pour un meilleur contrôle et une meilleure gestion des processus.

Le script Python suivant gère le partage de fichiers temporaire et permet d'utiliser Ctrl-C pour arrêter les services.

```python
#!/usr/bin/env python3
import subprocess
import time
import signal
import sys
import json
import requests

# Function to stop the HTTP server and ngrok
def cleanup(signum, frame):
    print("Arrêt du serveur HTTP et de ngrok...")
    if http_server_process:
        http_server_process.terminate()
    if ngrok_process:
        ngrok_process.terminate()
    sys.exit(0)

# Register the cleanup function for Ctrl+C
signal.signal(signal.SIGINT, cleanup)
signal.signal(signal.SIGTERM, cleanup)

# Initialize subprocess objects
http_server_process = None
ngrok_process = None

# Change to the share/temp directory
subprocess.run(["cd", "~/share/temp"], shell=True)

# Start the HTTP server
print("Démarrage du serveur HTTP sur le port 8080...")
http_server_process = subprocess.Popen(["python3", "-m", "http.server", "8080"])

# Start the ngrok tunnel
print("Démarrage du tunnel ngrok sur le port 8080...")
ngrok_process = subprocess.Popen(["ngrok", "http", "8080"], stdout=subprocess.PIPE)

# Wait a bit for ngrok to initialize and get the public URL
time.sleep(10)
response = requests.get("http://localhost:4040/api/tunnels")
ngrok_data = json.loads(response.text)
ngrok_url = ngrok_data['tunnels'][0]['public_url']

# Check if ngrok initialized properly
if not ngrok_url:
    print("Erreur : ngrok n'a pas pu initialiser le tunnel.")
else:
    print(f"Lien de partage : {ngrok_url}/")

# Wait for user to stop the HTTP server and ngrok
input("Appuyez sur [Enter] ou Ctrl+C pour arrêter le serveur et ngrok...")
cleanup(None, None)

```

Pour l'utiliser :

1. Rendez le script exécutable : `chmod +x NOM_DU_SCRIPT.py`
2. Exécutez le script : `./NOM_DU_SCRIPT.py`
3. Suivez les instructions à l'écran.

---

## Montrer des Applications Web 💻

Pour exposer une application web en développement, suivez les étapes ci-dessous :

1. Assurez-vous que votre application web est en cours d'exécution localement sur un port spécifique (par exemple, 3000).
2. Ouvrez un terminal et lancez la commande suivante :

```bash
ngrok http 3000
```

Cela créera un tunnel Ngrok vers votre application web locale, et vous pourrez partager l'URL générée.

---

## Utilisation 🚀

1. Rendez le script exécutable : `chmod +x NOM_DU_SCRIPT.py`
2. Exécutez le script : `./NOM_DU_SCRIPT.py`
3. Suivez les instructions à l'écran.

## Améliorations possibles 🛠️

- Ajout d'une interface utilisateur pour une utilisation encore plus facile.
- Intégration d'autres méthodes de partage de fichiers.
- NGROK permet d'utiliser des commandes pour automatiser le partage de fichiers et d'applications web. Pour plus d'informations, consultez la [documentation](https://ngrok.com/docs).
- Vous pouvez utiliser votre propre domaine personnalisé avec NGROK. Pour plus d'informations, consultez la [documentation](https://ngrok.com/docs#custom-domains).
- Vous pouvez utiliser docker pour exécuter NGROK. Pour plus d'informations, consultez la [documentation](https://ngrok.com/docs#docker-examples).
---

🎉🎉🎉🎉
