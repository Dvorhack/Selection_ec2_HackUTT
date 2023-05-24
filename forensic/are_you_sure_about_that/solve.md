# Are you sure about that ?

On a un fichier cat.rar, on commence par les 3 commandes pour savoir ce qu'est un fichier:
- file
- binwalk
- strings

`file` nous dit qu'il s'agit d'un rar

`binwalk` ne nous apporte rien de plus

`strings` ne donne rien de plus à première vue

on essaie donc de *unrar* mais on n'y arrive pas, il doit être corrompu.  
On regarde donc plus en détail la sortie de `strings` et on remarque des choses qui peuvent être familières: `IHDR`, `phYs`, `IDAT`, ...  
Il s'agit de nom de chunks PNG.

Le header PNG a surement été remplacé par un header RAR.  
On trouve le header PNG sur [wikipedia](https://fr.wikipedia.org/wiki/Portable_Network_Graphics): `89 50 4E 47 0D 0A 1A 0A`.  
Et on modifie le fichier avec [ce site](https://hexed.it/)

On récupère alors notre image