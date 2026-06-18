# librerias estabar de python
  ## cuales son
Categoría	Módulos
Sistema operativo	os, pathlib, shutil
Archivos y directorios	os, pathlib, glob
Fechas y tiempo	datetime, time, calendar
Matemáticas	math, statistics, decimal, random
Datos JSON	json
Expresiones regulares	re
Colecciones avanzadas	collections
Iteradores	itertools
Copias de objetos	copy
Compresión	zipfile, gzip
Redes e internet	urllib, http, socket
Multitarea	threading, multiprocessing, asyncio
Bases de datos	sqlite3
Registro de eventos	logging
Pruebas	unittest
Tipado	typing
  ## cualoes son lo mas usados 
Manipulación de archivos
import os
import pathlib

ruta = pathlib.Path("datos.txt")
Fechas y horas
from datetime import datetime

ahora = datetime.now()
print(ahora)
JSON
import json

datos = {"nombre": "Juan", "edad": 25}

texto = json.dumps(datos)
Matemáticas
import math

print(math.sqrt(25))
Números aleatorios
import random

numero = random.randint(1, 100)
Expresiones regulares
import re

texto = "correo@ejemplo.com"
patron = r"\w+@\w+\.\w+"

resultado = re.search(patron, texto)
Colecciones
from collections import Counter

contador = Counter(["a", "b", "a", "c"])
print(contador)
Registro de logs
import logging

logging.warning("Mensaje de advertencia")
Base de datos SQLite
import sqlite3

conexion = sqlite3.connect("mi_bd.db")
  ##  las formas de incluirlo en nuetros archivos de python
Importar el módulo completo
import math

print(math.pi)
print(math.sqrt(16))
Importar varios módulos
import os
import json
import random

También:

import os, json, random
Importar elementos específicos
from math import sqrt, pi

print(sqrt(25))
print(pi)
Importar todo (no recomendado)
from math import *

print(sqrt(25))

No se recomienda porque puede generar conflictos de nombres.

Importar con alias
import numpy as np

o con módulos estándar:

import datetime as dt

print(dt.datetime.now())
Importar funciones específicas con alias
from math import sqrt as raiz

print(raiz(36))
## modulos python
Un módulo es simplemente un archivo .py que contiene código reutilizable.

Ejemplo:

archivo: calculadora.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

archivo: main.py

import calculadora

print(calculadora.sumar(5, 3))

También:

from calculadora import sumar

print(sumar(5, 3))
