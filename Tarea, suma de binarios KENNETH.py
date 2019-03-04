#Entrada: Dos numeros binarios
#Salida: La suma de los dos numeros bianrios ingresados
#Restricciones: Deben ser numeros binarios del mismo tamaño (el que meta algo diferente está bateando xD).

def sumarBinarios(numero1, numero2):

    if isinstance(numero1, int) and isinstance(numero2, int) and (len(str(numero1)) == len(str(numero2))):
        return int(convertir(sumarAux(numero1, numero2, 0)))
    else:
        print("Ingresar una entrada válida")

def sumarAux(numero1, numero2, exp):

    if numero1 == 0:
        return 0
    else:
        return (numero1%10 + numero2%10)*(2**exp) + sumarAux(numero1//10, numero2//10, exp+1)

def convertir(a):

    if a == 0:
        return ""
    else:
        return convertir(a//2) + str(a % 2)

