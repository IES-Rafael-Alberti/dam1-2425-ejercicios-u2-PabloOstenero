#
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
#

def eco():
    frase = ""
    while frase != "salir":
        frase = input("Escribe la frase que quieres que repita o salir si quieres salir del programa: \n")
        if frase.lower() == "salir":
            print("Bye bye")
            frase = frase.lower()
        else:
            print(f"\n{frase}\n")


def main():
    eco()


if __name__ == "__main__":
    main()