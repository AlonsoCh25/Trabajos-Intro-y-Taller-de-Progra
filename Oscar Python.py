def suma_listas(lista , pollo):
    if isinstance(lista, list) and isinstance(pollo, list):
        return suma_lista_aux(lista, pollo)
    else:
        return "Error, lo que usted acaba de ingresar no es una lista"
def suma_lista_aux(lista, pollo):
    if lista == [] and pollo == []:
        return 0
    else:
        return lista [0] + suma_lista_aux(lista[0] + pollo[0])
    
        
