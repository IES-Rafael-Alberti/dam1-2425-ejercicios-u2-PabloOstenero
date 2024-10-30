#
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.
#

def numero_letra_en_frase(frase, letra):
    numero_letra = 0
    frase_min = frase.lower()
    for i in range(len(frase)):
        if frase_min[i] == letra:
            numero_letra += 1
    
    print(F"La letra {letra} está {numero_letra} veces en la frase {frase}")


def main():
    frase = input("Escribe una frase: ")
    letra = input("Escribe la letra que va a buscar en la frase: ")

    numero_letra_en_frase(frase, letra)


if __name__ == "__main__":
    main()