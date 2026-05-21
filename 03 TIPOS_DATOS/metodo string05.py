textos:str="hola"
print(textos.upper())
## metod para convertir enminuscula
texto_mayuscula:str="HOLAAA"
print(texto_mayuscula.lower())
## metodo para convertir solo la primer letra en mayuscula
texto:str=">buenos dias"
print(texto.capitalize())
## metodo para convertir la primera letra de cada paplbara rn mayuscula com un totulo
print(texto.title())

# metodo par quitar espacio
texto_espacio:str="           hola como estas        "
print(texto_espacio)
print(texto_espacio.strip())
# este emtodo quita los espacios que estan a ala dereecha e izquierda si deseaos solo  los specios de la izquierda usamos el lstrip y derecga rstrip
print(texto_espacio.rstrip())
# find retornara el indice donde comienza el texto a buscar si el texto no s eencurntra retorna
 
#parrafo:str=" mi mama me ama yo amio a mi mama de gianfranco"
#print(parrafo.find)("gianfranco")
#print(parrafo[35:])

# metodo para remplazar una parte de texto
texto_incorecto:str="ella es mala"
print("texto_incorrecto".replace("mala","buena"))
# metodo operador binario de xxistencia
# este operador verifica si cierto texto exisate oo no dentro de otro retorna true si exite y false si no
vocales:str="aeiouAEIOU"
print("a" in vocales)


# tarea averiguar que son y cuales son los operadores unarios binario terniarios
# unario

password_user :str=input("ingresa contraseña:")
print("bienvenido al sistema" if password_user=="hola1234"
      else "contraseña incorecta")
