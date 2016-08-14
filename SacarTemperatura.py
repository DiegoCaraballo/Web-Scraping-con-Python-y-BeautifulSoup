!/usr/bin/python
# -*- coding: utf-8 -*-
# Sitio: http://www.pythondiario.com
# Autor: Diego Caraballo
 
# Haciendo pruebas con BeautifulSoup y requests
 
# Importamos las librerias
from bs4 import BeautifulSoup
import requests
import time
import os
 
# Creamos el Bucle infinito
while True:
 
 # Capturamos la url 
 url = "http://www.timeanddate.com/weather/china/beijing"
 
 # Capturamos el hml de la pagina web y creamos un objeto Response
 r  = requests.get(url)
 data = r.text
 
 # Creamos el objeto soup y le pasamos lo capturado con request
 soup = BeautifulSoup(data, 'lxml')
 
 # Buscamos el div para sacar los grados
 temp = soup.find_all('div', class_="h2")
 
 # Buscamos el div para sacar la sensacion termica
 sTerm = soup.find_all('div', class_="clear")
         
        # Con [0] saco el primer elemento y con [1] el segundo
 print "La temperatura en Beijing: " + temp[0].text
 print "La sesacion termica: " + sTerm[1].text
  
 # Tiempo en segundos para ejecutarse nuevamente
 time.sleep(15)
  
 # Boramos los datos viejos, para Windows es "cls"
 os.system("clear")
