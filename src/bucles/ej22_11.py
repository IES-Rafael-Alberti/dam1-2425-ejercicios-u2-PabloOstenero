#
# Escribir un programa que pida al usuario una palabra 
# y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
#

def invertir_palabra(palabra):
    palabra_inv = ""
    for letra in palabra[::-1]:
        palabra_inv += letra

    return palabra_inv

def main():
    palabra = input("Escribe una palabra para invertirla: ")

    invertida = invertir_palabra(palabra)

    print(invertida)

if __name__ == "__main__":
    main()