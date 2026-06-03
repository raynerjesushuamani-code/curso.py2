# crear una lista dde 5 vertebrados animales  y 5 animales invertrebados el orden debera ser aleatorio
#""""
# 1.modificar los 3 primeros elementos por aves.
#2.modificar el 6 y el ultimo elemento por reptiles
#3.modificar el elemento 8 por gianfranco
#4.mostra toda la lista nueva con las modificaciones
animales:list=[    "perro","pulpo","caballo","caracol", "gato","araña","pez", "mariposa","elefante","medusa" ]
animales[0]="condor "
animales[1]="colibri"
animales[2]="aguila"
#2
animales[5]="iguana"
animales[-1]="anaconda"
#3
animales[7]="gianfranco"
#4
print(f"mi lista modificada es {animales}")
