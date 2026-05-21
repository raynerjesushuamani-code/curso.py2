# utilizar tecnicas para unir string en un solso concatenacion
## paare sto esto usamos el operador de concatenacion es el + caundo este oprador se encuentra entre dos textos se convierte ene l operador de conactenacon y cuando esta entre dos numeros es el operador de aadicion
nombre:str="noemi"
apellido:str="carrasco"
nombre_completo:str=nombre+" "+apellido
print(nombre_completo)
## opcon mas optima de concatenacion
print(nombre,apellido)

# f-tring(tarea)
# Formatode string con varioables de python y paar su uso se requiere de un f antes de escribir un streing sis e desa incluir codigo python ene l string se deberan encerrar  entre llaves 
nombre: str= "pepe"
edad:int=48
print(f"hola mi nombre es {nombre} y tengo {edad}")



nombre_cliente : str=  input("ingrese tu nombre")
ruc_cliente:int=int(input("ingresa ruc"))
direccion_cliente:str=input("dirigete direccion")
codigo_producto:str=input("ingrse codigo")
precio_unidad:float= float (input("el precio del producto"))
cantidad_producto:float = float(input("cantiodad a comprar"))
precio_total:float=precio_unidad*cantidad_producto
plantillas:str=f""
cliente: {nombre_cliente}
