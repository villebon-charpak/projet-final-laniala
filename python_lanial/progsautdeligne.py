# -*- coding: utf-8 -*-
"""
Created on Wed May 16 14:24:36 2018

@author: etudiant
"""
from os import path as os_path
PATH = os_path.abspath(os_path.split(__file__)[0])
monHTML=open("inconnu.txt","r")
data= monHTML.readlines()
data = [ d[:-2]+"<br>\n" for d in data ]
monHTML.close()
#data.replace('\r\n', "<br>")
#data.replace('\r\n \r\n', "<br>")
monHTML=open("inconnu.txt","w")
for d in data:
    monHTML.write(d)
monHTML.close()
print("ok")