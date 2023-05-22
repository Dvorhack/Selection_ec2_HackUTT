# Le cliché de César
## Raisonnement 
D'après l'énoncé, nous pouvons déduire que la méthode de chiffrement utilisée sur le fichier 'file.enc' est une méthode de décalage d'octets (*cf. Chiffrement César*)

On essaye tout d'abord de décaler octet à octet le fichier, en parcourant les 256 valeurs que peut prendre un octet. On remarque que cette méthode ne fonctionne pas et que l'on obtient rien de concret. 

On sait alors que les octets ne sont pas décalés de manière constante.

## Exploit
On choisit de travailler dans un premier temps avec les headers pour éviter de devoir process tout le fichier (c'est plus long sinon).

Pour trouver le header, on compare les n premiers bytes avec les signatures de fichiers connus (ici des images (*le titre nous indique "Le cliché de César", on peut donc déduire que l'on travaille avec des images*)). Dès que l'on a une égalité, on note le rang.

On ne remarque aucune cohérence pour le header png, alors que pour le header jpeg, on remarque un décalage de -1 à chaque rang.

On peut ainsi modifier le fichier en suivant le pattern, puis on obtient une image qui nous indique le flag.

