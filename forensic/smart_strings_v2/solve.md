# Smart Strings v2

On cherche donc un wallet XMR.  

Après quelques recherches internet, je trouve que cela correspond à une address Monero.  
Le format d'une addresse monero est une chaine de 95 caractères hexadécimaux.

Je fais donc un filtre pour trouver une chaine de ce format  
`strings my-own-garbagev2 |grep -E '[a-zA-Z0-9]{95}'`