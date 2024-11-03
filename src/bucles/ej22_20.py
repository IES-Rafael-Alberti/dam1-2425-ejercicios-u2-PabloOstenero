#
# Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). 
# Recorrer la frase, carácter a carácter, comparando con la letra buscada. 
# Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. 
# Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.
#

def posicion_letra(letra, frase):
    for i in range(len(frase)):
        if letra.lower() == frase[i].lower():
            print(f"La letra {letra} esta en la posicion {i+1} en la frase")


def busca_letra():
    frase = input("Escribe una frase: ")
    letra = input("Escribe la letra a buscar en la frase: ")
    
    if letra.lower() not in frase.lower():
        while letra.lower() not in frase.lower():
            error = len(frase) + 1
            print(f"La letra no está en la frase, probemos otra vez ({error})")
            letra = input("Escribe la letra a buscar en la frase: ")
            
            if letra.lower() in frase.lower():
                posicion_letra(letra, frase)
    else:
        posicion_letra(letra, frase)

def main():
    busca_letra()



if __name__ == "__main__":
    main()