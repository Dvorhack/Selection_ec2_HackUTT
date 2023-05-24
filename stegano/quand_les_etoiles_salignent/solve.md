# quand les etoiles s'alignent

Quand on ouvre l'image, on se rend compte qu'il y a juste des pixels blanc sur un fond noir.  
On peut donc se douter que les pixels codent de l'information.

Il faut aussi remarquer que les étoiles ne sont que sur la moitié basse de l'image.  
Pour rappel, la table ascii va de 0 à 127 soit la moitié des valeurs que peut prendre un octet. Coïncidence ? Je ne pense pas

On va donc parcourir l'image et récupérer la hauteur de chaque pixel blanc pour les convertir en ascii.

```python
from PIL import Image
import os

im = Image.open('star.png')
pix = im.load()


for x in range(0, im.size[0]):
    for y in range(0, im.size[1]):
        # On vérifie si c'est un pixel blanc
        if(pix[x, y] == 255):
            # On affiche la valeur de la hauteur
            # Pas besoin de changement d'échelle car l'image est de taille 255x255
            print(chr(y), end="")
```