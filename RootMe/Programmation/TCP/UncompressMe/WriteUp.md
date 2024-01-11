# TCP - Uncompress Me

## **15 Points**

### Programmation réseau

### Paramètres de connexion au challenge

## **Énoncé**
Pour commencer cette épreuve utilisant le protocole TCP, vous devez vous connecter à un programme sur une socket réseau.

 Vous devez décoder les chaînes de caractères compressées avec zlib et encodées en base64 envoyées par le programme.
 Vous devez renvoyer le message d’origine plusieurs fois.
 Vous avez 2 secondes pour envoyer la bonne réponse à partir du moment où le programme vous envoie la chaîne.
 La réponse doit être envoyée sous la forme de string.

### Paramètres de connexion au challenge

| Hôte | challenge01.root-me.org |
| --- | --- |
| Protocole | TCP |
| Port | 52022 |

## Solution

L'objectif est de faire un programme qui écoute en boucle les messages du serveur TCP donné. On doit dans un premier temps écouter le message du serveur, récupérer la string et la décode en base64, puis la décompresser avec zlib puis la décodé en base utf-8. [code ici](./uncompress_me.py)

```Bash
➜  UncompressMe git:(main) ✗ python3 uncompress_me.py
```