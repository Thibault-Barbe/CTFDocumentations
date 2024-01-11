import socket
import re
import codecs

# Paramètres du serveur
hote = 'challenge01.root-me.org'
port = 52021

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
    match = re.search(r"my string is '(.*?)'. What is your answer ?", donnees)

    if match:

        decoded_string = codecs.decode(match.group(1), 'rot13')+"\n"
        print(decoded_string)
        # Envoyer le résultat arrondi au serveur
        sock.sendall(decoded_string.encode('utf-8'))

        # Recevoir la réponse du serveur après avoir envoyé le résultat
        reponse_du_serveur = sock.recv(1024).decode('utf-8')
        print("Réponse du serveur:", reponse_du_serveur)

# Fermer la connexion
sock.close()