import socket
import re
import math

# Paramètres du serveur
hote = 'challenge01.root-me.org'
port = 52002

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
    match = re.search(r'Calculate the square root of (\d+) and multiply by (\d+)', donnees)
    
    if match:
        # Extraire les chiffres de la chaîne
        num1 = int(match.group(1))
        num2 = int(match.group(2))

        # Effectuer le calcul
        result = math.sqrt(num1) * num2

        # Arrondir le résultat à 2 chiffres après la virgule
        result_rounded = round(result, 2)

        # Envoyer le résultat arrondi au serveur
        sock.sendall(str(result_rounded).encode('utf-8'))
        print(f"Résultat envoyé: {result_rounded}")

        # Recevoir la réponse du serveur après avoir envoyé le résultat
        reponse_du_serveur = sock.recv(1024).decode('utf-8')
        print("Réponse du serveur:", reponse_du_serveur)

# Fermer la connexion
sock.close()

