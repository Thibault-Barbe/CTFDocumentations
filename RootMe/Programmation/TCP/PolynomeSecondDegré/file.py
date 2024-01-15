import socket
import re

# Paramètres du serveur
hote = 'challenge01.root-me.org'
port = 52018

# Création d'un socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
sock.connect((hote, port))
print(f"Connecté à {hote}:{port}")

def solve_quadratic(a, b, c):
    # Calcul du discriminant
    delta = b**2 - 4*a*c
    
    # Vérification du signe du discriminant
    if delta > 0:
        # Deux solutions réelles distinctes
        x1 = (-b + (delta**0.5)) / (2*a)
        x2 = (-b - (delta**0.5)) / (2*a)
        return "x1: " + str(round(x1, 3)) + " ; x2: " + str(round(x2, 3))
    elif delta == 0:
        # Une solution réelle double
        x = -b / (2*a)
        return "x: " + str(round(x, 3)),
    else:
        return "Not possible"


while True:
    donnees = sock.recv(1024).decode('utf-8')

    # Vérifier si la connexion est fermée
    if not donnees:
        break

    # Afficher les données reçues
    print("Données reçues:", donnees)

    t = re.search(r'Solve this equation please: (-?\d+).x² (.*?) (-?\d+).x¹ (.*?) (-?\d+) = (-?\d+)', donnees)

    if t:
        a = int(t.group(1))

        first_sign = 1 if t.group(2) == "+" else -1

        b = int(t.group(3)) * first_sign

        second_sign = 1 if t.group(4) == "+" else -1

        c = int(t.group(5)) * second_sign

        equal = int(t.group(6))

        print("a: ", a, "b: ", b, "c: ", c, "equal: ", equal)
        c = c + (equal * -1)

        res = solve_quadratic(a, b, c) + "\n"

        print("a: ", a, "b: ", b, "c: ", c)
        print(res)

        sock.sendall(res.encode('utf-8'))
    else:
        print("no t")


# Fermer la connexion
sock.close()