#Tarea numero 2 de Introduccion a la programacion.
#Kenneth Castillo Herrera 2019062984

##Ejercicio 1: Implemente una funcion que multiplique
#cada valor de la lista por su indice de posicion

def multiplicaciones(lista):
    if isinstance (lista, list):
        return mult_aux(lista, 0)
    else: return "El valor ingresado no es una lista"

def mult_aux(lista, indice):
    if lista == []:
        return []
    else:
        return [lista[0]*indice] + mult_aux(lista[1:], indice + 1)

#Ejercicio 2: Tome una lista de numeros que son elevados
#a al numero de su posicion sumando los resultados.
#Procese las sublistas.
def suma(lista):
    if isinstance (lista, list):
        return sumul_aux(lista, 1)
    else: return "Error el valor ingresado no es una lista"
def sumul_aux(lista, posicion):
    if lista == []:
        return 1
    if isinstance (lista[0], int):
        return lista[0]**posicion + sumul_aux(lista[1:], posicion + 1)
    else: return sumul_aux(lista[0] + lista[1:], posicion)

#Ejercicio 3: NO ENTIENDO

#Ejercicion 4: Intercambiar los digitos pares de un 
#numero con su pareja. Debe ser un entero.
def intercambiar(num):
    if isinstance(num, int) and contar(num, 0)%2 == 0:
        return inte_aux(num, 2, contar(num, 0))
    else: return "El valor ingresado no tiene longitud par"
def inte_aux(num, posicion, n):
    if num == 0:
        return 0
    else:
        return (((num%100)%10)*10**(posicion-1)+(((num%100)//10)*10**(posicion-2))+inte_aux(num//100, posicion+2, n))
def contar(num, contador):
    if num == 0:
        return 0
    if num > 0:
        return (contador + 1) + contar(num//10, contador)
    else: return
    
