# Ethereum - Tutoreum

## 20 Points

### Introduction

## Énoncé
Introduction a l’utilisation de Smart Contracts Ethereum avant d’entrer dans le vif du sujet.

## Solution

Tout d'abord faire:

```Console
level.locked().then(console.log)
```
On se rend compte alors que la variable locked est à false.

Il faut donc trouver le moyen de la débloquer, et on voit que le seul moyen c'est de faire appel à la fonction **own**.

Il faut donc trouver la clé pour pouvoir envoyer la même à la fonction own et valider la condition pour pouvoir rendre le **locked** à false.

On voit que la variable **key** est en public, on peut donc l'afficher:
```
level.key().then(console.log)
```

On obtient **you_got_me...**, on va donc appeler la fonction **own** avec la clé qu'on vient de trouver:

```
level.own('you_got_me...').then(console.log)
```
```Bash
level.locked().then(console.log)
true
```

On peut donc clicker sur le bouton **next** et avoir le flag.