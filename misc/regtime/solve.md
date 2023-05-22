# regtime

On voit que dans le format du flag, on nous demande de préciser le port utilisé par le C&C.  
On va donc faire une regex qui filtre les url où le port est spécifié  
`grep -E 'http://.+:[0-9]+' access.log`

On a donc l'url malveillante, plus qu'a la hasher pour avoir le flag  
`echo -n 'http://frplab.com:37566/sdhjkzui1782109zkjeznds' |sha256sum`