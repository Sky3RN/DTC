Créé le 13/11/2020 <br />
Corrigé le 26/02/2023

# DTC
Scrapper les 5 dernières quotes de DansTonChat.com

# Page web 
https://sky3rn.fr/?q=bashfr 

# Description du projet 
Si, comme moi, tu veux t'afficher les 5 dernières quotes de DansTonChat.com dans un terminal, j'ai développé un petit script en Python, utilisant BeautifoulSoup. Le script s'exécute toutes les heures grâce à la fonction time.sleep(3600) tout à la fin du code, où 3600 correspond à une valeur exprimée en secondes. En vrai, inutile de s'actualiser toutes les heures puisqu'il n'y a qu'un quote publiée par jour. <br />
Ça m'a pris environ 8h puisque je n'ai jamais touché à Python de ma vie, et je crois bien que je déteste ce langage maintenant ! Je me suis inspiré de plusieurs tutoriels que j'ai pu trouver sur Google et sur YouTube, et le résultat est plutôt concluant, mais j'ai bien galéré à faire fonctionner tout ça correctement..

# Quelques indications :
• Déjà, le charset, va savoir pourquoi mais en UTF-8 ça ne m'affichait pas ce que je souhaitais, chez moi, la méthode qui a fonctionné, c'est de passer ça en ISO-8859-1 (pour avoir les accents ET les smileys).<br />
• Ensuite, côté librairies pip et tout et tout, je n'ai pas pensé à noter tout ça, donc j'espère que tu t'y connais suffisamment pour installer ce qu'il te manque !<br />
• Les quotes s'affichent par ordre décroissant, la plus récente est tout en bas, pour passer en croissant il faut modifier range(4, -1, -1) en range(5)
<br /><br />
J'ai donc mis ça dans un fichier que j'ai nommé dtc.py je l'exécute simplement avec la commande python3 ! <br />
Personnellement, j'ai mis ça dans une fenêtre Conky qui est tout le temps affichée sur mon bureau sur Linux. 
