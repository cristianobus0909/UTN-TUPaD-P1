"""
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""
for i in range(101):
    print(i)
    
"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""
num = abs(int(input("Ingrese un numero entero: ")))


if num == 0:
    digitos = 1
    print("El numero ingresado tiene: ",digitos," digito")
else:
    digitos = 0
    while num > 0:
        num = num // 10
        digitos += 1
    print("El numero ingresado tiene: ",digitos," digitos")

"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""
num1 = int(input("Ingrese un numero"))
num2 = int(input("Ingrese otro numero"))

minimo = min(num1,num2)
maximo = max(num1,num2)
suma = 0

for i in range(minimo + 1, maximo):
    suma += i
    print(i)
print(f"La suma de los numeros entre {minimo} y {maximo} es: {suma}")

"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""
opc = 1
acc = 0
while opc == 1:
    num = int(input("Ingrese un numero: "))
    acc = acc + num
    opc = int(input("Ingrese 1 para continuar o 0 para salir: "))
print(acc)

"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
import random
numero_aleatorio = random.randint(0,9)
intentos = 0
opcion = True
while opcion:
    numero_usuario = int(input("Escriba un numero del 0 al 9 y adivine que numero estoy pensando"))
    if numero_usuario < 0 or numero_usuario > 9:
        print("Ingrese un numero valido entre 0 y 9")
    elif numero_usuario != numero_aleatorio:
        intentos += 1
        continue
    else:
        intentos += 1
        print(f"Ganaste!!! Adiviniste el numero en {intentos} intentos, tenes $1000000 de premio!!")
        opcion = False

"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
"""
for i in range(100,-1,-2):
    print(i)
"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""
suma = 0
num_del_usuario = int(input("Ingrese un numero positivo"))
if num_del_usuario > 0:
    for num in range(0,num_del_usuario):
        suma += num
        print(suma)
else:
    print("Ingrese un numero positivo")
"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""

pares = 0
impares = 0
positivo = 0
negativo = 0
for num in range(100):
    numero_usuario = int(input("Ingrese un numero: "))
    if numero_usuario < 0:
        if numero_usuario % 2 == 0:
            pares += 1 
            negativo += 1
        else:
            impares += 1
            negativo += 1
    elif numero_usuario > 0:
        if numero_usuario % 2 == 0:
            pares += 1 
            positivo += 1
        else:
            impares += 1
            positivo += 1
    else:
        print("Debe ingresar un numero")
print("Cantidad de numeros pares: ", pares)
print("Cantidad de numeros impares: ", impares)
print("Cantidad de numeros negativos: ", negativo)
print("Cantidad de numeros positivos: ", positivo)

"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""

suma = 0
acc = 0
for num in range(100):
    numero_usuario = int(input("Ingrese un numero: "))
    suma += numero_usuario
    acc += 1
promedio = suma / acc
print("La media de todos los numeros ingresados es: ", promedio)

"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""
numero_usuario = int(input("Ingrese un numero"))
invertido = ""
for num in str(numero_usuario):
    invertido = num + invertido 
print(invertido)