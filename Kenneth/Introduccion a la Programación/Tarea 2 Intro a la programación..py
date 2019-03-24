#Tarea numero 2 de Introduccion a la programación. 
#Kenneth Castillo Herrera 2019062984

##Ejercicio 1: Formar una lista a partir de los numeros
##pares de un numero. Se debe verificar que el numero
##ingresado es un entero positivo mayor a cero.

def formarlista(num):
    if isinstance (num, int) and num > 0:
        return formlist_aux(num)
    else: return "Error el valor ingresado no cumple con los parametros"
def formlist_aux(num):
    if num == 0:
        return []
    if (num%10)%2 == 0:
        return [num%10] + formlist_aux(num//10)
    else: return formlist_aux(num//10)

###Ejercicio 2: Programe una funcion que compruebe que
###un numero entero es un palindromo.

def palindromo(num):
    if isinstance (num, int) and num > 0: 
        return pal_aux(num, num, contar(num, 0))
    else: return "El valor ingresado nu cumple con las condiciones"
def pal_aux(num,num1, n):
    if num == 0:
        return True
    if num%10 == (num1//(10**(n-1))):
        return pal_aux(num//10, num1%10**(n-1), n-1)
    else: return False
def contar(num, contador):
    if num == 0:
        return 0
    if num > 0:
        return (contador + 1) + contar(num//10, contador)
    else: return
    
####Ejercicio 3: Contar las consonates de una cadena
####de texto.

def contarConsonantes(texto):
    if isinstance (texto, str):
        return conttext_aux(texto, 0)
    else: return "El valor ingresado no es admitido"
def conttext_aux(texto, contador):
    if texto == "":
        return 0
    if texto[0] == 'a':
        return conttext_aux(texto[1:], contador)
    if texto[0] == 'e':
        return conttext_aux(texto[1:], contador)
    if texto[0] == 'i':
        return conttext_aux(texto[1:], contador)
    if texto[0] == 'o':
        return conttext_aux(texto[1:], contador)
    if texto[0] == 'u':
        return conttext_aux(texto[1:], contador)
    else: return (contador+1) + conttext_aux(texto[1:], contador)

###Ejercicio 4: Intercambiar los valores de las posiciones
###con indice par, con las de indice impar.
def intercambiar(lista):
    if isinstance (lista, list) and len(lista)%2 == 0:
        return inte_aux(lista)
    else: return "El valor ingresado no es admitido"
def inte_aux(lista):
    if lista == []:
        return []
    else: return [lista[1], lista[0]] + inte_aux(lista[2:])
    
    
