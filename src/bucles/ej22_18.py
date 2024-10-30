#
# Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
# La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario 
# fueron números pares.
#

def mayor_num():
    num = 1
    pares = 0
    while num != -1:
        num = int(input("Escribe números enteros positivos o -1 para salir y ver el número de números pares ingresados: "))
        if num > 0 and num%2 == 0:
            pares += 1
    
    print(f"El número de pares introducidos es {pares}")

def main():
    mayor_num()

if __name__ == "__main__":
    main()