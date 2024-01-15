# AppArmor - Jail Introduction
## 15 Points
### Can’t you read ?

## Énoncé
Lors de la connexion au serveur de l’administrateur, un shell restreint via une politique AppArmor vous empêche de lire le flag bien que vous en soyez le propriétaire...

Trouvez un moyen de lire le flag à tout prix et passez outre la politique AppArmor mise en place dont voici la configuration :

```bash
#include <tunables/global>
 
profile docker_chall01 flags=(attach_disconnected,mediate_deleted) {
    #include <abstractions/base>
    network,
    capability,
    file,
    umount,
    signal (send,receive),
    deny mount,
 
    deny /sys/[^f]*/** wklx,
    deny /sys/f[^s]*/** wklx,
    deny /sys/fs/[^c]*/** wklx,
    deny /sys/fs/c[^g]*/** wklx,
    deny /sys/fs/cg[^r]*/** wklx,
    deny /sys/firmware/** rwklx,
    deny /sys/kernel/security/** rwklx,
 
    deny @{PROC}/* w,   # deny write for all files directly in /proc (not in a subdir)
    # deny write to files not in /proc/<number>/** or /proc/sys/**
    deny @{PROC}/{[^1-9],[^1-9][^0-9],[^1-9s][^0-9y][^0-9s],[^1-9][^0-9][^0-9][^0-9]*}/** w,
    deny @{PROC}/sys/[^k]** w,  # deny /proc/sys except /proc/sys/k* (effectively /proc/sys/kernel)
    deny @{PROC}/sys/kernel/{?,??,[^s][^h][^m]**} w,  # deny everything except shm* in /proc/sys/kernel/
    deny @{PROC}/sysrq-trigger rwklx,
    deny @{PROC}/kcore rwklx,
 
    /home/app-script-ch27/bash px -> bashprof1,
 
}
profile bashprof1 flags=(attach_disconnected,mediate_deleted) {
    #include <abstractions/base>
    #include <abstractions/bash>
   
    network,
    capability,
    deny mount,
    umount,
    signal (send,receive),
 
    deny /sys/[^f]*/** wklx,
    deny /sys/f[^s]*/** wklx,
    deny /sys/fs/[^c]*/** wklx,
    deny /sys/fs/c[^g]*/** wklx,
    deny /sys/fs/cg[^r]*/** wklx,
    deny /sys/firmware/** rwklx,
    deny /sys/kernel/security/** rwklx,
 
    deny @{PROC}/* w,   # deny write for all files directly in /proc (not in a subdir)
    # deny write to files not in /proc/<number>/** or /proc/sys/**
    deny @{PROC}/{[^1-9],[^1-9][^0-9],[^1-9s][^0-9y][^0-9s],[^1-9][^0-9][^0-9][^0-9]*}/** w,
    deny @{PROC}/sys/[^k]** w,  # deny /proc/sys except /proc/sys/k* (effectively /proc/sys/kernel)
    deny @{PROC}/sys/kernel/{?,??,[^s][^h][^m]**} w,  # deny everything except shm* in /proc/sys/kernel/
    deny @{PROC}/sysrq-trigger rwklx,
    deny @{PROC}/kcore rwklx,
 
    / r,
    /** mrwlk,
    /bin/** ix,
    /usr/bin/** ix,
    /lib/x86_64-linux-gnu/ld-*.so mrUx,
    deny /home/app-script-ch27/flag.txt r,
}
```

## Solution

L'objectif de ce challenge est de réussir à afficher le contenu du ficher /home/app-script-ch17/flag.txt. La subtilité de ce challenge est qu'on a les droits sur ce fichier, sauf que comme vu précédemment, on fait face à une politique AppArmor mise en place sur notre shell.

Il faut donc bien lire la mise en place de la politique et trouver une faille. on va directement sauter les choses qu'on nous refuse pour aller voir les choses dont on a droit:
```bash
/ r,
/** mrwlk,
/bin/** ix,
/usr/bin/** ix,
/lib/x86_64-linux-gnu/ld-*.so mrUx,
```

Pour comprendre les droits donnés on va se rendre le [AppArmor Hacktricks.](https://book.hacktricks.xyz/v/fr/linux-hardening/privilege-escalation/docker-security/apparmor)

Pour indiquer l'accès que le binaire aura aux fichiers, les contrôles d'accès suivants peuvent être utilisés :
- r (lecture)
- w (écriture)
- m (cartographie de la mémoire en tant qu'exécutable)
- k (verrouillage de fichier)
- l (création de liens durs)
- ix (pour exécuter un autre programme avec le nouveau programme - héritant de la politique)
- Px (exécuter sous un autre profil, après nettoyage de l'environnement)
- Cx (exécuter sous un profil enfant, après nettoyage de l'environnement)
- Ux (exécuter sans confinement, après nettoyage de l'environnement)

On va donc voir que d'après les droits donnés, on peut exécuter **/lib/x86_64-linux-gnu/ld-*.so** sans confinement, cet à dire en dehors de la politique AppArmor. Ce que à l'air très intéressant. On va donc essayer et faire:
```bash
/lib/x86_64-linux-gnu/ld-2.27.so /bin/cat flag.txt
[censorship]
```

On a donc eu raison de compter dessus, on a bien trouver une manière de contourner la jail.