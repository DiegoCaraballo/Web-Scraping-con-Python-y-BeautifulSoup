#!/usr/bin/python
# -*- coding: utf-8 -*-
# Sitio: http://www.pythondiario.com
# Autor: Diego Caraballo

# Haciendo pruebas con BeautifulSoup y requests

# Importamos las librerias
from bs4 import BeautifulSoup
import requests

# Capturamos la url ingresada en la variable "url"
url = raw_input("Ingrese la URL: ")

# Capturamos el hml de la pagina web y creamos un objeto Response
r  = requests.get("http://" +url)
data = r.text
print ""

# Creamos el objeto soup y le pasamos lo capturado con request
soup = BeautifulSoup(data, 'lxml')

# Capturamos el titulo de la página y luego lo mostramos
# Lo que hace BeautifulSoup es capturar lo que esta dentro de la etiqueta title de la url
titulo = soup.title.text
print "El titulo de la pagina es: " + titulo
print ""

# Buscamos todas etiquetas HTML (a) y luego imprimirmos todo lo que viene despues de "href"
for link in soup.find_all('a'):
    print(link.get('href'))

