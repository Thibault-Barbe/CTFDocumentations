# Solveur de polynômes du second degré
## 25 Points
### Rien ne sert de root quand on a les racines

## Énoncé
Votre professeur vous propose de vérifier vos compétences en maths et en automatisation, prouvez lui que vous êtes à la hauteur.

### Paramètres de connexion au challenge
| Hôte | challenge01.root-me.org |
| --- | --- |
| Protocole | TCP |
| Port | 52018 |

## Solution

Lorque l'on se connecte sur le tcp, on va reçevoir une consigne de résoudre un polynôme du second degré et d'envoyer le résulat sous le format suivant:
```bash
Output example for two roots => x1: -1337.777 ; x2: -7331.777
Output example for one root => x: -1337.995
Output example for no root => Not possible
```
Il faut donc, comme pour les précédent challenge, faire un script qui recçoit le message tcp, récupère les chiffres, et renvoie une réponse puis écoute la réponse du serveur TCP.

Pour cela je vais le faire en python. Tout d'abord, il faut faire en sorte d'écouter le serveur:
```Python
import socket
import re
import cmath

# Paramètres du serveur
hote = 'challenge01.root-me.org'
port = 52018

# Création d'un socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
sock.connect((hote, port))
print(f"Connecté à {hote}:{port}")
```

En suite, il faut récupérer tout les chiffres données pour le polynome du second degré:
```Python
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
```

Maintenant, la plus grosse partie, faire une fonction qui résoud le polynome:
```Python
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
```

La fin de notre fichier python avec l'envoie au serveur TCP:

```Python
res = solve_quadratic(a, b, c) + "\n"

print("a: ", a, "b: ", b, "c: ", c)
print(res)

sock.sendall(res.encode('utf-8'))
```

Et voilà, notre programme va donc envoyer les réponses au 25 polynomes d'affilé, et on va reçevoir le flag au bout de la 25ème bonne réponse !