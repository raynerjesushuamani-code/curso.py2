### una ferreteria  teine separada en dosnlistas los siguientes productos
"""
1. listas de productos de limpieza (10 peoductos)
2. lista de materilases de construccion 
el dueño desea realizar las siguiemtes acciones 
-----------------------------------------------------
el dueño desea realizar las siguiemtes acciones 
1. en su lista de productyos de limpieza existe un materila de construccion
debe eliminarlo y pasar el prodcuto a la lista que corresponde 
2. indica si en la lista de m.c existe cemento
3.em la lista p.l buscar el producto lejia y cambiar suvalor por lejia sapolio
4 mostrar un mensaje dondde se detalle cual es la lista de m.c y la lsita de p.l formateado
"""
producto_limpieza:list[str]=[ "lejia", "detergente", "jabon","desinfectante", "limpiavidrios", "esponja", "cera", "ambientador", "cemento","cloro"]
materiales_construccion:list[str]=["arena","ladrillo","yeso","fierro", "piedra", "madera","losas","tubos","clavos"]
#1 

elemnto_retirado=producto_limpieza.pop(producto_limpieza.index("cemento"))
materiales_construccion.append("elemnto_retirado")
print(materiales_construccion)
#2
existe:bool="cemento" in materiales_construccion
print(existe)
#3
posicion = producto_limpieza.index("lejia")
producto_limpieza[posicion] =("lejia sapolio") 
print(producto_limpieza)
#4
print("===== LISTA DE PRODUCTOS DE LIMPIEZA =====")
print( producto_limpieza)

print("===== materiales de construccion =====")
print(materiales_construccion)
