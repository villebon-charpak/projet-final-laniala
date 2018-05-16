# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:16:42 2018

@author: etudiant
"""

from os import path as os_path
PATH = os_path.abspath(os_path.split(__file__)[0])
monHTML = open("automatisation.txt","w") #mettre nom de votre fichier + le mettre dans le même dosser que le programme ;) 
#/!\ il faut faire tourner le programme avant d'écrire le contenu global de la page
labase="""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<!--
Ceci se passe de commentaire.
-->
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
 <meta http-equiv="Content-Language" content="fr" />
 <meta name="author" content="mettonblaze" />
 <title>
  Squelette
 </title>
  <link rel="stylesheet" href="feuilledestyle.css">
</head>
<body>
</p>
<hr />
</body>
</html>
"""
monHTML.write(labase)
monHTML.close()
print ("Merci Lola!")