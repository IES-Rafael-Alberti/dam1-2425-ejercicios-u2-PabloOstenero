#
# Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
#

def suma_digitos(num):
    if num <= 0:
        print("El número tenía que ser positivo.")
    elif num < 10:
        print(f"La suma de los dígitos es {num}")
    else:
        suma = 0
        num = str(num)
        for i in range(len(num)):
            suma += int(num[i])
        print(f"La suma de los dígitos es {suma}")

def main():
    num = int(input("Escriber un número positivo para sumar sus dígitos: "))

    suma_digitos(num)


if __name__ == "__main__":
    main()