#
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
#

def muestra_palabra(palabra):
    for i in range(10):
        print(palabra)

def main():
    palabra = input("Ingrese un palabra: ")

    muestra_palabra(palabra)


if __name__ == "__main__":
    main()