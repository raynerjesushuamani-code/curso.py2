# DICCIONARIOS 
SON LAS FORMAS MA COMUUN DE ALMACENAR DAOS ESTRUCTURADOS DE OBJETOS QUE NOS RODEAN DEL MUNDOa ligual quer las lista que guaedan informacion en `elementos`  de igual amnera los diccionarios alamcenan sus datos en `elementos` separados pro coma 
la diferencia es que las listas almacenan los elementos por `indice y valor`
ylosdiccionarios lamcenan los `elemntos` por `clave:valor`
***ejemplo**
```python
vocales:list[str]=['a','e','i','o','u']
# indices           0   1   2   3   4 
# un elemento en un alista estaconformado por dos cositas el indice y su valor 
vocales[2]
alumno:dict={'nombre':'eduardo','edad':40}
# para acceder a un diccionario
alumno["nombre"] # eduardo
```
## aceder a elementos
- **por clave(forma directa)**
 ```python
 persona:diccionario={
    "nombre":"celia",
    "edad":16,
    "ciudad":"cabo verde",
    "email":"celi@email.com"
 }
 print(persona["edad"])
 print(persona[email])
```
- ** por su metdo (forma segura)**
```python
persona:diccionario={
    "nombre":"celia",
    "edad":16,
    "ciudad":"cabo verde",
    "email":"celi@email.com"
 }
 print(persona.get("nombre"))
# la diferencia de ste mentodo es que no permite manejar errores
print(persona.get("telefono"))
print(persona.get("telfono","no disponible")) # si l calve telefono no existe no mostra none sino el segundo poarametro que le pasemos al metodo get.
```
## modifivar elementos
```python
persona:diccionario={
    "nombre":"celia",
    "edad":16, 
 }
 perosona["edad"]=19
 # agregar una nueva clave:valor
 persona["carrera"]="agro"
 ## agregar/actualizar multiples elemntos
 para esto tenmos que hacer uso de el emtodo 'update'
 se puede agregar si lo pares de 'clave:valor' no existey actualizar si el 'clave:valor' exsiste.
```
```python
tienda:dict[str:str|int]={
    "razon_social":"bigote",
    "ruc":20607890
# actualizar usasndo el metdod update tengo dos metodos 
# 1. diccionarios
tienda.update({"ruc":123456789,"telefono":987654321})
# 2. pares clave=valor 
tienda.updaate(h_atencion="9-12",gerente="kevin")
}
```
## eliminar elementos
```python
el_eliminado=tienda.pop("ruc")
tienda.popitem() # elimina el ultimo elemento 
# para limpiar el diccionario
tienda:clear()
## recorrer un diccionario(tarea)