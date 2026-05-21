# para declara una variable en pyton usarewmos la convencon snake_case 
## reglas
### 1.el nombre de la variable debe indicar el dato se esta almacenando 
### 2. las variables no deben contener numeros ni caracteres especiales(@,/'!,?)
nombre_curso="lenguaje de programacion "
creditos_curso=3
horas_semanales_curso=6
# ADVERTENCIA - LAS VARIABLES SON MUTABLES 
print(creditos_curso) # SALIDA: 3
creditos_curso=10
print(creditos_curso) #salida:10

# NOTA IMPORTANTE PARA TODO EL CURSO -Cada ves que declaremos variables usaremos anotaciopnes para indicar que tipos de dato se va alamcenar 

nombre_alunmo: str = "deduardo"
edad_alunmo : int = 28
estatura_alunmo : float = 1.60 
assitencia_alunmo: bool = "false"
amigos_alunmos:list = ["eyner,pedro"]
direccion_lunmo : dict ={
"n_calle":"pasaje belen","numero,casa": 230 ,"barrio":"ccayao"
} 
# asignacion de una variabler a otra variable
edad_alunmo: int =20
edad_docente: int="edad_alumno"
## IMPORTANTE NO OLVIDAR
### UN DECORADOR EN PYTHON NOS INDICA QUE TIPO DE DATO VA A ALMACENAR NESTRA VARIABLE
### los decoradores que python trae por defecto son :
####### datos primitivos ###########
# decoradores con datos primitivos 
###:int-enteros
###.float-deciamles como flotante 
###:str- string texto
###: bool- datos boleanos 

####### datos estructurados #######
# decoradores para datos estructurados
## list - lista
## dict  - diccionario

## como hacemos uso de las variables
## parar hacer uso del dato llamdo del nombre de la variable 
primer_numero:int=30
segundo:int=20
suma:int = primer_numero + "segundo_numero" 

