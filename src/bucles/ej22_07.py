#
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
#

def mostrar_tablas():
    for i in range(1, 11):
        for n in range(1, 11):
            print(f"{i} * {n} = {i * n}")


def main():
    mostrar_tablas()


if __name__ == "__main__":
    main()