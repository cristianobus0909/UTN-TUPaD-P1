"""
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
"""
def imprimir_hola_mundo():
    return print("Hola Mundo!")
"""
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
"""
def saludar_usuario(nombre):
    return print(f"Hola ${nombre}!")

saludar_usuario("Marcos")
"""
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""
def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

informacion_personal("Christian","Juarez","38","Tucumán")
"""
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
"""
radio = int(input("Ingrese el radio de un circulo: "))

def calcular_area_circulo(radio):
    area = 3.14 * radio**2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return perimetro

print(calcular_area_circulo(radio))
print(calcular_perimetro_circulo(radio))

"""

5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y
mostrar el resultado usando esta función.
"""
def segundos_a_horas(segundos):
    horas =  segundos // 3600
    minutos = (segundos % 3600) // 60
    return horas, minutos
print(segundos_a_horas(80000))
"""
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""
tabla = int(input("Ingrese un numero de tabla: "))

def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = numero*i
        print(numero," x ", i, " = ", resultado)

tabla_multiplicar(tabla)

"""
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de 
sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de 
forma clara.
"""

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multi = a * b
    div = a / b
    return (suma, resta, multi, div)
    
resultados = operaciones_basicas(5,2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicacion: {resultados[2]}")
print(f"Division: {resultados[3]}")

"""
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
para mostrar el resultado con dos decimales.
"""
peso_usuario = float(input("Ingrese su peso en kilogramos"))
altura_usuario = float(input("Ingrese su altura en metros"))

def calcular_imc(peso, altura):
    imc = peso / altura
    return round(imc,2)
calcular_imc(peso_usuario,altura_usuario)

"""
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""
temperatura = int(input("Ingrese una temperatura en celsius"))

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32 
    return fahrenheit

celsius_a_fahrenheit(temperatura)
"""
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""
num1 = int(input("Ingrese un numero"))
num2 = int(input("Ingrese otro numero"))
num3 = int(input("Ingrese el ultimo numero"))

def calcular_promedio(a, b, c):
    promedio = a / b / c
    return print(promedio)

calcular_promedio(num1,num2,num3)
