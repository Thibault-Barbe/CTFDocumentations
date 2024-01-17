# Eh oui, parfois
## 10 Points
### Ne cherchez pas trop compliqué

## Énoncé
Rendez vous dans la section d’administration.

## Solution

Pas grand chose à dire pour ce challenge.

Lorsqu'on lance le challenge on tombe sur une page web. Comme on sait que notre objectif est d'aller dans la partie admin, on essaie directement d'aller sur /admin. On tombe sur un login form qui bloque l'accès à la page.

Ma permière intuition était de tester un brute force avec hydra et l'utilisatuer **admin**:
```bash
hydra -l admin -P /usr/share/wordlists/metasploit/unix_password.txt challeng01.root-me.org http-get /realiste/ch3/admin/index.php
```

Mais aucun résultat. Je suis donc parti sur l'éxamination de la requête http avec l'outil BurpSuite. J'utilise le proxy pour faire inteférence et récupérer la requête à la page. Je me rappelle avoir déjà fait un challenge similaire ou le but était de changer la méthode de la requête en autre chose que GET ou POST dans l'objectif de bypass le form bloquant.
J'envoie donc la requête dans le repeater, puis change le GET en OPTIONS. BINGO ! Je tombe sur la page et on me donne le flag du challenge.