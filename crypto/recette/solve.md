# Recette

On récupère un message à décoder au format Hexadécimal. On pourra utiliser la plateforme Cyberchef pour faire les opérations : https://cyberchef.org/

Hexadécimal : 32 69 31 73 34 69 31 73 38 64 31 6f 31 64 31 6f 38 69 31 6f 32 39 64 31 6f 33 34 69 31 6f 38 64 31 6f 39 69 31 6f 32 38 64 31 6f 37 32 69 31 6f 34 34 64 31 6f 32 64 31 6f 33 37 69 31 6f 35 30 64 31 6f 36 31 69 31 6f 31 38 64 31 6f 33 32 64 31 6f 31 32 69 31 6f 32 33 69 31 6f 31 33 69 31 6f 37 32 64 31 6f 32 34 69 31 6f 33 39 69 31 6f 33 64 31 6f 33 37 64 31 6f 31 64 32 6f 32 35 69 31 6f 32 31 69 31 6f 33 38 64 31 6f 31 32 69 31 6f 33 33 64 31 6f 32 64 31 6f 31 32 69 31 6f 31 30 64 31 6f 36 69 31 6f 38 64 31 6f 32 36 69 31 6f 31 64 31 6f 31 33 64 31 6f 34 37 69 31 6f

Format réduit (obtenu en déchiffrant depuis l'héxadécimal) : 2i1s4i1s8d1o1d1o8i1o29d1o34i1o8d1o9i1o28d1o72i1o44d1o2d1o37i1o50d1o61i1o18d1o32d1o12i1o23i1o13i1o72d1o24i1o39i1o3d1o37d1o1d2o25i1o21i1o38d1o12i1o33d1o2d1o12i1o10d1o6i1o8d1o26i1o1d1o13d1o47i1o

On nous indique ensuite de le développer de manière à ne plus voir les chiffres, puis on nous indique que l'étape d'après sera de le décoder depuis le DeadFish. Après s'être renseigné sur le format, on voit qu'il n'est composé que de **i**, de **s**, de **d** et de **o**. On se dit alors qu'il faut écrire n fois la lettre qui suit le numéro :

*Ex : 4d devient dddd*

Deadfish : iisiiiisddddddddodoiiiiiiiiodddddddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiioddddddddoiiiiiiiiioddddddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiioddddddddddddddddddddddddddddddddddddddddddddoddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiioddddddddddddddddddddddddddddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiioddddddddddddddddddoddddddddddddddddddddddddddddddddoiiiiiiiiiiiioiiiiiiiiiiiiiiiiiiiiiiioiiiiiiiiiiiiioddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiioiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiodddodddddddddddddddddddddddddddddddddddddodooiiiiiiiiiiiiiiiiiiiiiiiiioiiiiiiiiiiiiiiiiiiiiioddddddddddddddddddddddddddddddddddddddoiiiiiiiiiiiiodddddddddddddddddddddddddddddddddoddoiiiiiiiiiiiioddddddddddoiiiiiioddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiododddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiio

On utilise le site dcode pour décoder le deadfish obtenu :

87?"D<E)qECh6saAMdq)Ahe@??XmGS20<280JI<k

Puis on suit la dernière étape et on décode depuis la Base85 pour obtenir le flag:

Flag: HackUTT{le_de4d_f1sh_c_e5t_c00l}