# Baby reverse 2

On ouvre le fichier dans Ghidra pour voir à quoi il ressemble.  
![main func](imgs/main.png)

Cette fois ci c'est l'entrée utilisateur qui est modifiée puis comparée à une chaine, on ne peut donc pas utiliser la même méthode que précédemment.  
Cependant, la modification est relativement simple: chaque octet est décalé de 2

On peut donc récupérer le flag est le programme suivant:  
```python
flag  = 0x7d5656576d65634a.to_bytes(8, 'little')
flag += 0x6135757435783574.to_bytes(8, 'little')
flag += 0x77686136.to_bytes(4, 'little')

for i in flag:
    print(chr(i-2),end='')
print()
```