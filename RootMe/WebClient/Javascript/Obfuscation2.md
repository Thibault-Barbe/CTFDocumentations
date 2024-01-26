# Javascript - Obfuscation 2
facebooklinkedintwitter
## 10 Points

## Énoncé
Descendons de 3 étages...

## Solution

Tout ce trouve dans le code source, il faut récupérer le code js obfusquer et tout d'abord le décoder grace à CyberChef avec URL decode. Récupérer le résultat et refaire un URL decode avec ce qu'il y a dans le unescape.

On s'apperçoit donc de la fonction fromCharCode, ce qui signifie qu'il faut qu'on utiliser le From Charcode de CyberChef. On va régler en base 10 et récupérer l'output.
Ce qui nous donne le flag.