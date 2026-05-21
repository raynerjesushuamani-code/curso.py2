



Operadores unarios, binarios y ternarios

Los operadores son símbolos o palabras especiales que sirven para realizar operaciones sobre datos, valores o variables dentro de un programa. Dependiendo de cuántos elementos necesiten para funcionar, los operadores se clasifican en unarios, binarios y ternarios.

Operadores unarios

Los operadores unarios trabajan con un solo operando. Esto significa que la operación se aplica únicamente a una variable o valor.

Se utilizan para cambiar el signo de un número, aumentar o disminuir valores, o negar condiciones lógicas.

Características
Solo necesitan un dato.
Son operaciones simples y rápidas.
Se usan mucho en matemáticas y lógica.
Ejemplos
Negación numérica
x = 8
print(-x)

Resultado:

-8

Aquí el operador - cambia el signo positivo a negativo.

Negación lógica
x = True
print(not x)



Operadores binarios

Los operadores binarios trabajan con dos operandos. Son los más utilizados en programación porque permiten hacer operaciones matemáticas, comparaciones y cálculos entre dos valores.

Características
Necesitan dos datos.
Se usan para sumar, restar, comparar y combinar valores.
Son fundamentales en casi todos los programas.
Ejemplos matemáticos
Suma
a = 5
b = 3
print(a + b)

Resultado:

8
Multiplicación
print(a * b)

Resultado:

15
Ejemplos de comparación
print(a > b)

Resultado:

True

El operador > compara dos valores.

Ejemplos de operadores binarios comunes
Operador	Función
+	suma
-	resta
*	multiplicación
/	división
%	módulo o residuo
==	igualdad
>	mayor que
<	menor que
Operadores ternarios

Los operadores ternarios trabajan con tres operandos. Se utilizan principalmente para evaluar condiciones de forma corta y rápida.

Son una versión resumida de una estructura if-else.

Estructura general

En muchos lenguajes:

condición ? valor_si_verdadero : valor_si_falso

En Python:

valor_si_verdadero if condición else valor_si_falso
Ejemplo en Python
edad = 20
mensaje = "Adulto" if edad >= 18 else "Menor"
print(mensaje)

Resultado:

Adulto
Equivalencia con if-else

El operador ternario hace lo mismo que:

if edad >= 18:
    mensaje = "Adulto"
else:
    mensaje = "Menor"

Pero usando menos líneas.

Diferencias principales
Tipo de operador	Cantidad de operandos	Ejemplo
Unario	1	-x
Binario	2	a + b
Ternario	3	"Sí" if x else "No"
Importancia en programación

Estos operadores son esenciales porque permiten:

realizar cálculos,
comparar datos,
tomar decisiones,
modificar variables,
simplificar código.

Sin operadores, los programas no podrían procesar información correctamente.

Ejemplo completo
x = 10
y = 5

# Operador unario
print(-x)

# Operador binario
print(x + y)

# Operador ternario
resultado = "Mayor" if x > y else "Menor"
print(resultado)

Resultado:

-10
15
Mayor