#
# Escribe el algoritmo burbuja
#

def es_numero(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def ordena(a):
    cadena = ""
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if float(a[j+1]) < float(a[j]):
                aux = a[j]
                a[j] = a[j+1]
                a[j+1] = aux

    for i in range(len(a)):
        if i == len(a)-1:
            cadena += a[i]
        else:
            cadena += a[i] + " "

    return cadena

def burbuja(numeros):
    try:
        for i in range(len(numeros)):
            if not es_numero(numeros[i]):
                raise ValueError

        ordenado = ordena(numeros)
        return ordenado
    except ValueError:
        return "La cadena está mal creada."

def main():
    numeros = input("Escribe una lista de números: \n")
    numeros = numeros.split(" ")
    print(numeros)
    numeros = burbuja(numeros)

    print(numeros)

if __name__ == "__main__":
    main()