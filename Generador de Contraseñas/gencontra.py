import random #selecciona caracteres aleatorios
import string #proporciona el conjunto de caracteres 

def generar_contrasena(longitud):
    # Garantizar al menos un carácter de cada tipo
    mayuscula = random.choice(string.ascii_uppercase)
    minuscula = random.choice(string.ascii_lowercase)
    numero = random.choice(string.digits)
    especial = random.choice("!@#$%&*+-_?")

    # Combinar todos los caracteres posibles
    todos = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        "!@#$%&*+-_?")

    # Crear lista inicial con los caracteres obligatorios
    contrasena = [mayuscula, minuscula, numero, especial]

    # Completar hasta la longitud deseada
    for _ in range(longitud - 4):
        contrasena.append(random.choice(todos))

    # Mezclar para que los obligatorios no queden siempre al inicio
    random.shuffle(contrasena)

    return "".join(contrasena)


def menu():
    while True:
        print("\n===== GENERADOR DE CONTRASEÑAS =====")
        print("1. Seguridad Leve (8 caracteres)")
        print("2. Seguridad Media (12 caracteres)")
        print("3. Seguridad Alta (16 caracteres)")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            longitud = 8
        elif opcion == "2":
            longitud = 12
        elif opcion == "3":
            longitud = 16
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")
            continue

        contrasena = generar_contrasena(longitud)

        print("\nContraseña generada:")
        print(contrasena)

        repetir = input("\n¿Desea generar otra contraseña? (S/N): ").upper()

        if repetir != "S":
            print("Programa finalizado.")
            break


menu()
