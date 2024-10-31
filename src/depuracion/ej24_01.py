#
# Escribe el algoritmo burbuja
#

def burbuja(a):
    cadena = ""
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j+1] < a[j]:
                aux = a[j]
                a[j] = a[j+1]
                a[j+1] = aux

    for i in range(len(a)):
        if i == len(a) - 1:
            cadena += a[i]
        else:
            cadena += a[i] + ", "

    return cadena


def main():
    numeros = input("Escribe una lista de números separados por , y un espacio: \n")
    numeros = numeros.split(", ")
    try:
        for i in range(len(numeros)):
            if (not numeros[i].isdigit()):
                raise ValueError

        ordenado = burbuja(numeros)
        print(ordenado)
    except ValueError:
        print("La cadena está mal creada.")

if __name__ == "__main__":
    main()