# Fichier fou

Quand on ne sait pas ce qu'est un fichier, il y a 3 choses à regarder:
- file
- binwalk
- strings

`file` ne nous donne rien

`binwalk` indique de la donnée **Zlib** 

`strings` nous donne beaucoup de choses, notamment ça finit par **IEND** donc le fichier doit être une image PNG corrompue

On commence donc par vérifier pourquoi file n'as pas détecté que c'est un PNG (i.e. le magic byte doit être cassé)
D'après [wikipédia](https://fr.wikipedia.org/wiki/Portable_Network_Graphics), un fichier PNG doit commencer par "89 50 4E 47 0D 0A 1A 0A"  
Or notre fichier commence par "0d 0a 1a 0a", les 4 premiers octets ont été retirés.  
Une fois ajoutée, file nous dis bien que c'est un PNG mais on ne peut l'afficher pour autant

Le format PNG est sous forme de chunk, on va donc vérifier l'intégrité de nos chunks avec [ce site](https://www.nayuki.io/page/png-file-chunk-inspector)  
On voit que le 3e chunk est cassé et notamment son type est BITX avec X un octet non imprimable. C'est donc certainement un chunk sBIT et un octet est manquant.  
Ici c'est la taille du chunk qui est manquant, on peut calculer la distance avec le prochain chunk (gAMA).
On trouve une distance de 0x10 octets et si l'on enlève la taille du CRC, du champ type, ... on trouve une taille de 4

Avec 4 comme taille de notre chunk sBIT, on récupère notre image !