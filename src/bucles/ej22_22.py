#
# Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. 
# Por cada número, informar cuántos dígitos pares y cuántos impares tiene. 
# Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
#
import os
import time

def pares_e_impares():
    numeros = -1
    digito = ""
    while numeros != "0":
        pares = 0
        impares = 0
        numeros = input("Escribe un número positivo para comprobar los números pares e impares o 0 si quieres salir: \n")
        if numeros != "0":
            for i in range(len(numeros)):
                digito = numeros[i]
                if int(digito) % 2 == 0:
                    print(f"El dígito nº {i+1} ({digito}) es par")
                    pares += 1
                else:
                    print(f"El dígito nº {i+1} ({digito}) es impar")
                    impares += 1
        
            print(f"El número {numeros} tiene {pares} dígitos pares y {impares} dígitos impares")

            time.sleep(5)
            os.system("cls")
        else:
            print("Bye bye...")


def main():
    pares_e_impares()


if __name__ == "__main__":
    main()