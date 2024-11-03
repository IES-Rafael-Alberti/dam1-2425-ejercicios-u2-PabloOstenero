#
# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
#

def mayor_num():
    num = 1
    mayor = 0
    while num != 0:
        num = int(input("Escribe números enteros positivos o 0 para salir y ver el número mas alto ingresado: "))
        if num > mayor:
            mayor = num
    
    print(f"El número más alto de los números introducidos es {mayor}")

def main():
    mayor_num()

if __name__ == "__main__":
    main()