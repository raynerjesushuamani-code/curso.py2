alumnos:list[str]=['deduardo','noemi','victo','emerson','yo']
print(alumnos)
#eliminar  por inidce
alumnos.remove ('yo')
print(alumnos)
# elimiar el ultim valor por defecto
alumnos.pop()
print(alumnos)
# pop tambien elimina elementos por indice  tiene ka cractersitica e recupara el elemnto elminado eso quiere decir que podemso almacenarlos
a=alumnos.pop(1)
print(f"eliine: {a}")
print(f"mi lista de seaprobados sera:{alumnos}")
## tengo una lsita de marcasde vehiculos(toyota,nisan,datsun,daewod,simomack,mazda.honda),crear un programam que realize lo siguiente
"""
1. eliminar el 5 elemento
2. en swu lugar agregar la marca mitsubishi
3. buscar nisan y mostrrar su valor por el terminal
4. mostrar si existe honda en mi liosta de vehiculos
"""
vehiculos = ["toyota", "nisan", "datsun", "daewod", "simomack", "mazda", "honda",]
vehiculos.pop(4)
vehiculos.insert (4,"mitsubishi")
posicion = vehiculos.index("nisan")
print("La marca nisan está en la posición:", posicion)
existe:bool="honda" in vehiculos
print(existe)
print(vehiculos)
