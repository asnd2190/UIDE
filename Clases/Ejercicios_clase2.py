#solicitar al usuario su edad y determinar si es mayor de
#edad o no
edad = input("ingrase su edad: ")
if not edad.isdigit():
    print("Ingrese un numero del 1 al 100")
elif int(edad) >= 18: 
    print("Usted es mayor de edad")
else:
    print("Usted no es mayor de edad")

#ingresa 3 numeros son iguales o no y si alguno es igual
#a otro e indicar cuales son iguales
n1= int(input("Ingrese el primer numero: "))
n2= int(input("Ingrese el segundo numero: "))
n3= int(input("Ingrese el tercer numero: "))
if n1 == n2 == n3:
    print("Los tres numeros son iguales")
elif n1 == n2:
    print("El primer numero es igual al segundo numero")
elif n1 == n3:
    print("El primer numero es igual al tercer numero")
elif n2 == n3:
    print("El segundo numero es igual al tercer numero")
else:
    print("Los tres numeros son diferentes")


#ingresar un usuario y contraseña y verificar 
#si son correctos, el usuario es admin y la contraseña es 1234
us = input("Ingrese su usuario: ")
pw = input("Ingrese su contraseña:")

if us == "admin" and pw == "1234":
    print("Bienvenido admin")
else:
    print("Usuario o contraseña incorrectos")


#ingresar un numero y determinar si es positivo, negativo o cero
num = input("Ingrese un numero: ")
if not num.lstrip("-").isdigit():
    print("Ingrese un numero valido")
elif int(num) > 0:
    print("El numero es positivo")
elif int(num) < 0:
    print("El numero es negativo")
else:    
    print("El numero es cero")