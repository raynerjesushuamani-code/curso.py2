lista_vacia:list=[]
print(len(lista_vacia))
# por regla el nombre de  la variable no debe tener el tipo de dato que  se va a almacenar
amores:list[str]=["wicho","pococha","cesar"]
print(f"cantida de elementos es {len(amores)}")
frutas:list[str]=['🍎','🥝','🍆','🍑','🍌','🍉']
# posicion indice
## acceder al 3er elemento
print(frutas[2])
# acceder al 2 elemento po rindice negativo
print(frutas[-3])
frutas[-1]="🍊"
print(frutas)

ciudades:list[str]=['lima','cusco', 'chincha','pausa','urcus']
# si deseamos que los datos extraidos sean persistentes osea se mantengan almacenado durante la ejecucion de mi programa los almacena en una variable 
datos_extraidos:list[str]=ciudades[-2]
# si lo deseo mostrar y no almacenar el slicing lo realizo en el print

print(ciudades[0:3])
print(datos_extraidos)
## Renplazo de elementos por slicing
num_pares:list[int]=[1,3,5,6,8,10]
print(num_pares)
num_pares[0:3]=[2,4]
print(f"milista modificada es {num_pares}")
