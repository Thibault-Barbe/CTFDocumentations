# Suite mathématique

## 20 Points
### Renvoyer le résultat d’une suite mathématique en moins de deux secondes ? Qui a dit impossible ?

## Énoncé
Réussissez à renvoyer le résultat d’une suite mathématique en moins de deux secondes.

## Solution

Tout d'abord, on récupère tous les chiffres nécessaire pour pouvoir faire le calcul:

```Pyhton
import requests
import re

get = requests.get('http://challenge01.root-me.org/programmation/ch1/')
print(get.text + "\n")
cookies = get.cookies
html_content = get.text

first = re.search(r" (-?\d+) \+ U<sub>n</sub> \] (.*?) \[ n \* (-?\d+) ", html_content)
second = re.search(r"U<sub>0</sub> = (-?\d+)\n", html_content)
third = re.search(r'You must find U<sub>(\d+)</sub>', html_content)

if first:
    addNumber = int(first.group(1))
    operation = 1 if first.group(2) == "+" else -1
    multiplyNumber = int(first.group(3))
    print("Addition Number:", addNumber)
    print("opeation: ", operation)
    print("Multiplication Number:", multiplyNumber)

if second:
    result = int(second.group(1))
    print("U<sub>0</sub>:", result)

if third:
    target_n = int(third.group(1))
    print("Target n:", target_n)
```

En suite, l'objectif va être de faire une boucle qui va utilisé la logique de calcul de la suite que l'on a sur la page html que l'on a GET:
```Pyhton
i = 1
while( i <= target_n):
    result = (addNumber + result) + (((i-1) * multiplyNumber) * operation)
    i = i + 1
```
Il faut bien faire attention de commencer à 1 car comme on a déjà U0, cela ne sert à rien de le recalculer et notre résultat sera donc éronné. En suite, il faut bein faire attention de faire i-1 lorsque que l'on nous demande de faire n * [chiffre], care pour calculer n+1 il faut utiliser n, or, dans le code on va utiliser i qui est égal à n+1, donc pour pouvoir avoir n, il faut faire i - 1.

Après la fin de ce calcul, il faut tout simplement faire une requête GET comme indiqué sur la page du site, sans oublié de mettre les cookies pour que le site reconnaisse que le résultat vient de la même session que celui qui fait le premier GET:

```Pyhton
print(f"U<sub>{i}</sub> = {result}")
print(result)

res = get = requests.get('http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result='+str(result), cookies=cookies)
print(res.text)
```

On obtient donc le flag si on envoit un bon résultat.