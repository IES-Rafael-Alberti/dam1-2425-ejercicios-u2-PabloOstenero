#
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.
#


def main():
    num2 == 0
    num1 = float(input("Escribe un número: "))
    
    while num2 == 0:
        num2 = float(input("Escribe otro número: "))
        if num2 == 0:
            print("El segundo número no puede ser 0")

    print(f"La división de {num1} y {num2} es {num1/num2}")

if __name__ == "__main__":
    main()