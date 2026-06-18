# modulo y libreria estandar
# libreria estandar typing tipar adtos  alist y diccionarios para hacer mas optino el codigo
# modulo es unnaporcion de codigon utilizable para poder usrlo necesitamos importar laparde del codigo

alummno:dict[str:str|int]
from typing import Union
# SIN LIBRERIA

alummno:dict[:Union[str,int,float,bool]]={
    "id_alumno":1,
    "nombre":"mio",
    "dni":211263157234,
    "nombre":"mio",
    "edad":20,
    "matricula":True
}
#acceder 
print(alummno["dni"])
# print(alummno["tricula"])
## metodoss
print(alummno.get("edad","valor no ncontrado"))
# crear /modificar
print(alummno)
alummno["nombre"]="tuyo" # si existe la clave lo actuañiza
print(alummno)
alummno["ruc"]="902030349" #si no existre lo crea
# crear modificar varios
alummno.update({"nombre":"celia","edad":15})
alummno.update({"carrera":"agro","semestre":"III"})
print(alummno)
# eliminar
eliminado=alummno.pop("carrera")
print(f"el elmentos eliminado es: {eliminado}")
print(f"mi nuevo diccionario {alummno}")
