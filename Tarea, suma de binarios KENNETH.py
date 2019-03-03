#Entrada: Dos numeros binarios
#Salida: La suma de los dos numeros bianrios ingresados
#Restricciones: Deben ser numeros binarios de misma longitud (el que meta algo diferente está bateando xD).

def sumabin(bin1, bin2):

    if isinstance(bin1, int) and isinstance(bin2, int) and (len(str(bin1)) == len(str(bin2))):
        return int(convertir(sumarAux(bin1, bin2, 0)))
    else:
        print("Ingresar una entrada válida")

def sumarAux(bin1, bin2, exp):

    if bin1 == 0:
        return 0
    else:
        return (bin1%10 + bin2%10)*(2**exp) + sumarAux(bin1//10, bin2//10, exp+1)

