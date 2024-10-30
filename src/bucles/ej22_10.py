#
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
#

def primo_o_no_primo(num):
    no_primo = False
    for i in range(2, int((num/2)+1)):
        if num % i == 0:
            no_primo = True
    
    if no_primo == True:
        print("El número no es primo")
    else:
        print("El número es primo")


def main():
    num = int(input("Escribe el número entero que quieras comprobar si es primo: "))

    primo_o_no_primo(num)


if __name__ =="__main__":
    main()