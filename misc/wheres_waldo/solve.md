# Where's Waldo

On cherche donc le seul fichier unique, pour cela on va comparer leur hash.  
C'est faisable de plusieurs manières mais le plus simple reste bash car une seule ligne suffit  
`md5sum dataset/* |cut -d' ' -f1|sort |uniq -u`