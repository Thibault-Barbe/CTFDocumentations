import socket
import re
import math
import base64

# Paramètres du serveur
hote = 'challenge01.root-me.org'
port = 52023

# Création d'un socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
sock.connect((hote, port))
print(f"Connecté à {hote}:{port}")

# Boucle pour écouter les données
while True:
    # Recevoir les données du serveur
    donnees = sock.recv(1024).decode('utf-8')

    # Vérifier si la connexion est fermée
    if not donnees:
        break

    # Afficher les données reçues
    print("Données reçues:", donnees)

    # Utiliser une expression régulière pour extraire les chiffres de la chaîne
    match = re.search(r"my string is '(.*?)'", donnees)
    
    if match:
        # Extraire les chiffres de la chaîne
        decoded_string = base64.b64decode(match.group(1)).decode('utf-8')+"\n"
        print("decoded string: ", decoded_string)
        # Envoyer le résultat arrondi au serveur
        sock.sendall(decoded_string.encode('utf-8'))

        # Recevoir la réponse du serveur après avoir envoyé le résultat
        reponse_du_serveur = sock.recv(1024).decode('utf-8')
        print("Réponse du serveur:", reponse_du_serveur)

# Fermer la connexion
sock.close()