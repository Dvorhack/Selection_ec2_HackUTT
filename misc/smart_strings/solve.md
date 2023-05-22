# Smart strings

On a peu d'information pour avoir le flag, tout ce qu'on sait c'est qu'il est pas en clair.
Pour vérifier s'il n'est pas stocké avec un encodage basique, il existe l'outil [String cheese](https://github.com/MathisHammel/stringcheese).

Si l'on connait le format du flag, il va essayer de le chercher en UTF-16, base64, ...  
`stringcheese HackUTT --file my-own-garbage`