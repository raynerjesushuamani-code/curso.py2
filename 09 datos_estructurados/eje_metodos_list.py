## deseamos agregra en una lista vacia los nombre de los paises que partciparan en el mundial desarrolar el programa que haga posible esta tarea 
paises:list[str]=[]
paises.append("peru")
paises.append("bolivuia")
print(paises)
## manera 2
pais:str=input("ingresa el nombre del pais")
paises.append(pais)
print(paises)
## manera 3
rango:int=int(input("ingrse la cantidad de paises que va ingresar"))
for i in range(rango): 
    nuevos_paises:str=input("ingrese un pais")
    paises.append(nuevos_paises)
    print(paises)
