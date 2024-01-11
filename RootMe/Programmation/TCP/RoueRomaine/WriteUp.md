# TCP - La roue romaine
## 10 Points
### Programmation réseau

## Énoncé
Pour commencer cette épreuve utilisant le protocole TCP, vous devez vous connecter à un programme sur une socket réseau.

Vous devez décoder la chaîne de caractères encodée en ROT13 envoyée par le programme.
Vous avez 2 secondes pour envoyer la bonne réponse à partir du moment où le programme vous envoie la chaîne.
La réponse doit être envoyée sous la forme de string.

### Paramètres de connexion au challenge

| Hôte | challenge01.root-me.org |
| --- | --- |
| Protocole | TCP |
| Port | 52021 |

## Solution

Faire un fichier Python qui communique avec le serveur TCP en écoutnat le serveur, en récupérant la string, la décodant avec l'algorithme ROT13, l'envoyer puis re-écouter le serveur. [code ici](./roue_romaine.py)

```Bash
$ python3 roue_romaine.py
```