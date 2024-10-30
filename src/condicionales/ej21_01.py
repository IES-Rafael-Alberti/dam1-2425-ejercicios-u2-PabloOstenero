#
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
#

MAYORIA_EDAD = 18

def comprueba_mayor(edad):
    if edad >= MAYORIA_EDAD:
        print("Eres mayor de edad, toma una cervecita.")
    else:
        print("Eres menor de edad, mejor toma un zumo.")


def main():
    edad = input("Cuál es tu edad: ")
    salir = False

    while not salir:
        try:
            edad = int(edad)
            salir = True
        except ValueError:
            print("Eso no es un número.")
            edad = input("Cuál es tu edad: ")

    comprueba_mayor(edad)


if __name__ == "__main__":
    main()