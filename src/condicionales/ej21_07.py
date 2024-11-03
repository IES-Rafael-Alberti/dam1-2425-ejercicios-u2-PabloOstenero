#
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
#

def pide_renta():
    renta = float(input("Escribe tu renta anual: "))
    return renta

def calcula_tipo_impositivo(renta):
    if renta < 10000:
        print("El tipo impositivo correspondiente es 5%")
    elif renta < 20000:
        print("El tipo impositivo correspondiente es 15%")
    elif renta < 35000:
        print("El tipo impositivo correspondiente es 20%")
    elif renta < 60000:
        print("El tipo impositivo correspondiente es 30%")
    else:
        print("El tipo impositivo correspondiente es 45%")

def main():
    renta = pide_renta()

    calcula_tipo_impositivo(renta)


if __name__ == "__main__":
    main()