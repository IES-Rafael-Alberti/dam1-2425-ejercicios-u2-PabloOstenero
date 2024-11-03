#
# Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
#

def suma_digitos(num):
    if num <= 0:
        resultado = "El número tenía que ser positivo."
    elif num < 10:
        resultado = f"La suma de los dígitos es {num}"
    else:
        suma = 0
        num = str(num)
        for i in range(len(num)):
            suma += int(num[i])
        resultado = f"La suma de los dígitos es {suma}"

    return resultado

def main():
    num = int(input("Escriber un número positivo para sumar sus dígitos: "))

    resultado = suma_digitos(num)

    print(resultado)


if __name__ == "__main__":
    main()