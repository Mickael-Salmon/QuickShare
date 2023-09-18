#!/usr/bin/env python3
import subprocess
import time
import signal
import sys
import json
import requests
from colorama import Fore, Style
from tqdm import tqdm

def start_ngrok(port):
    global ngrok_process
    print(f"{Fore.GREEN}Démarrage du tunnel ngrok sur le port {port}...{Style.RESET_ALL}")
    ngrok_process = subprocess.Popen(["ngrok", "http", str(port)], stdout=subprocess.PIPE)

    # Wait a bit for ngrok to initialize and get the public URL
    for _ in tqdm(range(10)):
        time.sleep(1)
        
    response = requests.get("http://localhost:4040/api/tunnels")
    ngrok_data = json.loads(response.text)
    ngrok_url = ngrok_data['tunnels'][0]['public_url']

    # Check if ngrok initialized properly
    if not ngrok_url:
        print(f"{Fore.RED}Erreur : ngrok n'a pas pu initialiser le tunnel.{Style.RESET_ALL}")
    else:
        print(f"{Fore.BLUE}Lien de partage : {ngrok_url}/{Style.RESET_ALL}")

def cleanup(signum, frame):
    print(f"{Fore.YELLOW}Arrêt du serveur HTTP et de ngrok...{Style.RESET_ALL}")
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

# Ask user for the type of sharing
choice = input(f"{Fore.MAGENTA}Quel type de partage souhaitez-vous ?\n1) Partage de fichiers\n2) Partage d'application web\nChoix: {Style.RESET_ALL}")
if choice not in ['1', '2']:
    print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")
    sys.exit(1)

# Ask user for the port number
port = input(f"{Fore.CYAN}Entrez le numéro du port sur lequel démarrer le service (par exemple, 8080 ou 3000): {Style.RESET_ALL}")

# Start the appropriate service based on the user choice
if choice == '1':
    print(f"{Fore.GREEN}Démarrage du serveur HTTP sur le port {port}...{Style.RESET_ALL}")
    http_server_process = subprocess.Popen(["python3", "-m", "http.server", port])
    start_ngrok(port)

elif choice == '2':
    print(f"{Fore.GREEN}Assurez-vous que votre application web est en cours d'exécution sur le port {port}...{Style.RESET_ALL}")
    start_ngrok(port)

# Wait for user to stop the HTTP server and ngrok
input(f"{Fore.YELLOW}Appuyez sur [Enter] ou Ctrl+C pour arrêter le serveur et ngrok...{Style.RESET_ALL}")
cleanup(None, None)
