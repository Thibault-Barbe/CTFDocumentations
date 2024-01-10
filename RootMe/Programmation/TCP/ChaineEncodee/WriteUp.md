# TCP - Chaîne encodée

## 10 Points

### Programmation réseau

### Énoncé

Pour commencer cette épreuve utilisant le protocole TCP, vous devez vous connecter à un programme sur une socket réseau.

Vous devez décoder la chaîne de caractères encodée envoyée par le programme.

Vous avez 2 secondes pour envoyer la bonne réponse à partir du moment où le programme vous envoie la chaîne.

La réponse doit être envoyée sous la forme de string.

### Paramètres de connexion au challenge

| Hôte | challenge01.root-me.org |
| --- | --- |
| Protocole | TCP |
| Port | 52023 |

## Solution
Ecrire un fichier en python qui écoute, parse et répond au serveur tcp puis reécoute pour recevoir la réponse avec le flag [ici](./retour_au_coll%C3%A8ge.py)

L'objectif était de récupérer la string que le serveur TCP nous donne puis lui renvoyer décodée.

```Bash
$ python3 chainde_encodee.py
Connecté à challenge01.root-me.org:52023
Données reçues: 
==================
 ENCRYPTED STRING 
==================
Tell me the clear content of this string !

my string is 'R25MS1NDYjFMeVE1NWQ5WWhHWWtQaQ=='. What is your answer ? 
decoded string:  GnLKSCb1LyQ55d9YhGYkPi

Réponse du serveur: [+] Good job ! Here is your flag: RM{TCP_Enc0d3_4nd_D3c0d3}
```