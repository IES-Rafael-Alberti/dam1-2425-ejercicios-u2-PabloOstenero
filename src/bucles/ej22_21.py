#
# Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
# (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
# cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, 
# no se debe procesar y se debe pedir que ingrese un nuevo monto. 
# Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, 
# se le debe aplicar un 10% de descuento.
#

def procesar_montos():
    ventas = 0
    monto = -1
    while monto != 0:
        monto = float(input("Escribe el monto a pagar: "))
        if monto > 0:
            ventas += monto
        elif monto < 0:
            print("El monto no puede ser negativo.")
    
    if ventas >= 1000:
        print(f"El total a pagar es ${(ventas - (ventas*0.1)):.2f} con su descuento por haber superado los $1000.")
    else:
        print(f"El total a pagar es ${ventas:.2f}.")

def main():
    procesar_montos()


if __name__ == "__main__":
    main()