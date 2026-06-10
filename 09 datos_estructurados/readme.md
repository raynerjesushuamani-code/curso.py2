#    DATOS ESTRUCTURADOS ⚡ 
- tenos 3 tipos de dato primarios(string,numerico,booloeano)
- tenemos 2 tipos de datos estruvturados (listas,diccionarios)
## listas
son la manera de como python puede organizar multiples tipos de datos enuna sola variable
se puede tener:
- lista de tipo mnumerticos
- lista de tipos de texto
- listas de tipo mixto
python nos permite acceder a esats lisats a traves de Indices, los indices son acendentes empesando del numero 0.
### Creacion de listas  
para listas solo basta cerrar los elementos que deseamos almacenar con `[]`inmediantamente despues del operador de asignacion `=`
```python
# crando una lista vacia
lista:list=[]
# lista numerica
## ojote: los elementos de una lista se separan por comas
lista_numerica:list[int]=[3,8,4,5,8]
lista_numero_mixto:list[int|float]=[3.6,7,.7]
# lista de texto
amigos:list[str]=["eduardo","reyner",""]
# listas mixtas
listas_mixtas:list=["pedro",20,false,1.67]
```
### acceder y modificar elementos de una lista
para poder acceder a un elemento de la lista trabajamos con los indcises que python le asigna a vcada elemnto tenemos:
- los indices positivos (comienzan en 0 y van de la izquierda haciab la derecha)
- los indices negativos (comienza en -1 y van de derecha a al izquierda)
con estos indices podemos acceder a los elementos:
- por indice (posicion)
- por rango (slicing)
```python
frutas:list[str]=['🍎','🥝','🍆','🍑','🍌','🍉']
# posicion indice
## acceder al 3er elemento
print(frutas[2])
# acceder al 2 elemento po rindice negativo
print(frutas[-3])
```
## modificar
list [-1]="🍊"
list(frutas)
## Diccionario
acceder por rango 
```python
vocales:str=['a','i','e','o','u']
## estra tecnica nos permite acceder a ams de un elemento en una sola linea de codigo
vocales[0:3]
## slicing
ciudades:list[str]=['lima','cusco', 'chincha','pausa']
ciudades[0:3]
print(ciudades)
## reemplazar elementos por slicing
vocales[0:3]=['A','E','I']
```
### metodo para listas
es un accion que opuedo realizar en ua lista los metododsd por lo general se utilizan despues de las variables y se accede al metodo a travez de puntos .
los metodos mas comunes son aquello que nos permite agregar modificar y eliminar
```python
# agregar elementos
## apend
animales:list[str]=[]
animales.append
animales.append
## el metod apend agrga los elementos siempre en l aultimaq posicion de la lista 
## insert
numeros_pares:list[int]=[4,6,10]
numero_pares.insert(0,2)
numero_pares.insert(3,8)
amigos:list[str|int]=["juan","jose"]
amigos_insert(1,"deduardo")
vocales:list[str]=["a","b","c","d"]
vocales.remove("u")
# ultimo elemento
vocales:list[str]=["a","b","c","d"]
vocales.pop(3)
```
