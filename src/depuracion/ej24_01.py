#
# Escribe el algoritmo burbuja
#

def es_numero(num):
    """
    Comprueba que los elementos de la lista son números.

    Args:
        num (str): Elementos de la lista para comprobar si es un número

    Returns:
        True si el parámetro es un número o False si no lo es

    """
    try:
        float(num)
        return True
    except ValueError:
        return False

def ordena(a):
    """
    Ordena los números de la lista.

    Args:
        a (list[str]): Contiene los datos a ordenar
        cadena (str): Cadena formada por los datos ordenados para devolver

    Returns:
        str: La cadena con los números ordenados
    
    """
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
    """
    Comprueba que la cadena esté bien creada y llama a la función ordena para que ordene 
    los datos en el caso de que la cadena sea correcta.

    Args:
        numeros (list[str]): Lista recibida desde main
        ordenado (str): Cadena con los números ordenados
    
    Returns:
        str: La cadena con los números ordenados o un mensaje de error si la cadena no esta bien hecha.

    """
    try:
        for i in range(len(numeros)):
            if not es_numero(numeros[i]):
                raise ValueError

        ordenado = ordena(numeros)
        return ordenado
    except ValueError:
        return "La cadena está mal creada."

def main():
    """
    Función principal que ejecuta el programa.

    Crea la cadena de caracteres con los números y los separa, mandándolos después a la función para que los ordene.
    Después de recibir la cadena con los números ya ordenados (o un mensaje de error si la cadena no esta bien formada)
    muestra el resultado por pantalla.

    """
    numeros = input("Escribe una lista de números: \n")
    numeros = numeros.split(" ")

    numeros = burbuja(numeros)

    print(numeros)

if __name__ == "__main__":
    main()