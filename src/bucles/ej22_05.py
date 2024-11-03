#
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
#

def mostrar_capital(invertir, interes, años):
    for i in range(1, años+1):
        invertir *= (1 + (interes/100))
        if i == 1:
            print(f"El capital tras {i} año será {invertir:.2f}")
        else:
            print(f"El capital tras {i} años será {invertir:.2f}")

def main():
    invertir = float(input("Escribe una cantidad a invertir: "))
    interes = float(input("Escribe el interés anual: "))
    años = int(input("Escribe cuántos años va a tenerlo: "))

    mostrar_capital(invertir, interes, años)

if __name__ == '__main__':
    main()