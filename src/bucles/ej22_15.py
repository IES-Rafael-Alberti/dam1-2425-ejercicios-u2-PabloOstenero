#
# Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
# Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
#

def suma_num():
    suma = 0
    num = 1
    while num != 0:
        num = int(input("Escribe números enteros a sumar o 0 para salir y ver el resultado: "))
        if num > 0:
            suma += num
    
    print(f"La suma de los números introducidos es {suma}")

def main():
    suma_num()

if __name__ == "__main__":
    main()