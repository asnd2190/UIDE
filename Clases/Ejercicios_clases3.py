#ingrse 3 numeres que se multipliquen y que sea con while
cnta=1
multi=1
while cnta<=1:#este 3 es las veces que se repite cuantos numeros se solicitan
    num=int(input("Ingrese un numero: "))
    multi*=num
    cnta+=1
print("El resultado de la multiplicacion es: ", multi)


#ingrese el numero ganador si el numero es igual al ganador se imprime un mensaje
#de felicitaciones sino se imprime otro mensaje usando en while
ganador=7
num=int(input("Ingrese un numero ganador: "))
while num!=ganador:
    print("Lo siento, intente de nuevo")
    num=int(input("Ingrese otro numero ganador: "))
print("Felicitaciones, has adivinado el numero ganador")