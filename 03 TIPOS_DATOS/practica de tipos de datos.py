## crear haciendo el uso de las clases anteriores una calculadora
## que pida al usaria dos numeros enteros y luego de manera ordenada mostrar por el terminal el rersultado




mensaje_bienvenida:str=""""""
""""""


print(mensaje_bienvenida)
print("a continuacion ingrese dos numeros para la suma")
numero_uno:int=int(input("imgrese el primer numero:"))
numero_dos:int=int(input("imgrese el segundo numero numero:"))
resultado_suma:int=numero_uno+numero_dos
mensaje_resultado:str=f"""
    el resultado de la suma del numero
    {numero_uno}
    con el numero
    {numero_dos}
    es igual a {resultado_suma}
    """
print(mensaje_resultado)
