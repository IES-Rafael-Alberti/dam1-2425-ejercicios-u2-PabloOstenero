#
# Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga 
# (en caso de haber más de una, mostrar la primera) y cuántas palabras había. 
# Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
#

def palabra_mas_larga(frase):
    palabra = ""
    for i in range(len(frase.split(" "))):
        if len(frase.split(" ")[i]) > len(palabra):
            palabra = frase.split(" ")[i]

    print(f"La palabra más larga de la frase {frase} es {palabra}")


def main():
    frase = input("Escribe una frase para que diga que palabra es la más larga: \n")
    palabra_mas_larga(frase)


if __name__ == "__main__":
    main()