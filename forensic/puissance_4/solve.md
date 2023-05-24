# Puissance 4

La première chose que je fais est de vérifier les messages de commits du projet git.  
On trouve quelques commit  
```bash
# git log
commit 425499cbbdf28e2ea812fcc3a49343d16f978d95 (HEAD -> master)
Author: Yanis <megayanis@live.fr>
Date:   Sat Oct 8 16:40:42 2022 +0200

    some modifications in ./src/

commit e3ac18592bcee07812f0ad6d5ef4544f6f361c90
Author: Yanis <megayanis@live.fr>
Date:   Sat Oct 8 16:38:39 2022 +0200

    i learned how to create zip files

commit 13103983f60b072fe85c7ed945f5c26d7067fb4b
Author: Yanis <megayanis@live.fr>
Date:   Sat Oct 8 16:35:17 2022 +0200

    removed the server folder

commit 1bec85150a5f63fe7981c64531858ae43d6a55d4
Author: Yanis <megayanis@live.fr>
Date:   Sat Oct 8 16:34:17 2022 +0200

    first commit
```

Ensuite le parcours les différents commit via `git show <commitID>`

Dans un des commit, on voit un commentaire supprimé qui donne un lien pastebin  
```bash
# git show 13103983f60b072fe85c7ed945f5c26d7067fb4b
-public Server {
-
-//TODO
-
-// SSH creds can be found there : https://pastebin.com/44X8jyvE
-
-}
```  
Mais ce pastebin est protégé par un mot de passe

Après avoir fouillé le git, je n'ai rien trouvé d'autre. Je me suis donc attaqué au code.  
Mais le zip *test.zip* est protégé par un mot de passe.

On va donc casser le mot de passe  
```
zip2john test.zip > hash
john hash
```

Et on trouve un mot de passe.  
Ce mot de passe permet également de déverrouiller le pastebin