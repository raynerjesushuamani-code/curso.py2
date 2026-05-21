# este tipon de datosirve para alamcenar informacion de tipo de texto texto simpl o txto extenso
# para almacenar un dato de tipo texto la informacion debera estar encerada entre comillas ("",'',"""").
## - comillas dobles ("")
## - comillas simples ('')
## dcostring ("""""",'''''')
nombre_instituto: str = "IESTP-JMA"
NOMBRE_CURSO : str = """
el curso de "lenguajede programacion",
tiene un duracion de un semestre
educativo con 6 horas semanales y
aprender a programar  en el lenguaje
"python"
 """
## los stirng tienen funciones basicas para poder interactuar con los datos que estamos alamcenando
## la estructuyra de una funcion es la siguiente
## nombre_funcion(argumentos)ç
## argumento-es un valor que se le pasa a un funcion en base a su programacion retornara otro valor dsitinto al pasado por el argumento 
# funcioon para mostrar informacion por terminal
print("hola mundo") # salida:hola mundo
print("hola,mundo")# salida; hola mundo
# funcion para mostrar la cantidad de caracteres que tiene un string-texto
texto:str = "suy deduardo y tu eres ser guey"
cantidad_caracteres:int = len(texto)
print(cantidad_caracteres)

# forma de acceder a un caracter en especial 
## para esto asemos uso de la anotacion corchete[
## para esto teemos quen entender que python asigna a cada caracter con un indice base 
# ejemplo:celia
#~ indice 01234
nombre_celia:str ="celia_come_verga" 
print("nombre_celia come verga" )
print("nombre_celia come verga" [2])
# troceado de texto 
## paar esto se utiliza la notacion de corchetes conn la diferencia que se debe indicar de qe indce hasta que indice inicial y un indice final del texto a extraer 
## texto[ i_inicial: i_final]
vocales:str = "aeiou"
print(vocales[1:3])
print(vocales[3:])
print(vocales[:3])
## f string
