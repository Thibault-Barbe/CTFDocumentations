import socket
import re
import zlib
import base64

# Paramètres du serveur
hote = 'challenge01.root-me.org'
port = 52022

# Création d'un socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
sock.connect((hote, port))
print(f"Connecté à {hote}:{port}")

# Boucle pour écouter les données
while True:
    # Recevoir les données du serveur
    while True:
        donnees = sock.recv(1024).decode('utf-8')

        # Vérifier si la connexion est fermée
        if not donnees:
            break

        # Afficher les données reçues
        print("Données reçues:", donnees)

        # Utiliser une expression régulière pour extraire les chiffres de la chaîne
        match = re.search(r"my string is '(.*?)'. What is your answer ?", donnees)

        if match:

            decoded_string = base64.b64decode(match.group(1))
            print(decoded_string)
            decompressed_string = zlib.decompress(decoded_string)
            print(decompressed_string)
            print(decompressed_string.decode())
            # Envoyer le résultat arrondi au serveur
            sock.sendall((decompressed_string.decode()+"\n").encode('utf-8'))

# Fermer la connexion
sock.close()