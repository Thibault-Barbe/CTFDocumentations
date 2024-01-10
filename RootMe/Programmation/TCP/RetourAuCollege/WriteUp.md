# TCP - Retour au collège

## 5 Points

### Programmation réseau

### Énoncé

Pour commencer cette épreuve utilisant le protocole TCP, vous devez vous connecter à un programme sur une socket réseau.

Vous devez calculer la racine carrée du nombre n°1 et multiplier le résultat obtenu par le nombre n°2.

Vous devez ensuite arrondir à deux chiffres après la virgule le résultat obtenu.

Vous avez 2 secondes pour envoyer la bonne réponse à partir du moment où le programme vous envoie le calcul.

La réponse doit être envoyée sous la forme de int ou float

### Paramètres de connexion au challenge

| Hôte | challenge01.root-me.org |
| --- | --- |
| Protocole | TCP |
| Port | 52002 |

## Solution

Ecrire un fichier en python qui écoute, parse et répond au serveur tcp puis reécoute pour recevoir la réponse avec le flag [ici](./retour_au_coll%C3%A8ge.py)

L'objectif est de récupérer les chiffres envoyer par le serveur TCP pour pouvoir faire le calcul demandé et envoyer le résultat en réponse.

```
$ python3 retour_au_college.py
```