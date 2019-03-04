def lenn(x):
    if x== [ ]:
        return 0
    else:
        return 1+ lenn(x[1:])
    
def suma_bin(lista1,lista2,acarreo):
    if isinstance(lista1, list):
        if isinstance(lista2, list):
            if isinstance(acarreo, int):
                 if lenn(lista1) == lenn(lista2):
                    return  suma_bin_aux(lista1,lista2,acarreo,lenn(lista1) - 1)
                 else:
                    return "Las listas deben tener la misma longitud"
            else:
                    return "Falta el acarreo"
        else:
            return "El segundo elemento debe ser una lista"
    else:
         return"El primer elemento debe ser una lista"

def suma_bin_aux(lista1,lista2,acarreo,i):
    if i == -1:
        if acarreo == 1:
            return [1]
        else:
            return [ ]
    else:
        if acarreo == 0:
            if lista1 [i] ==1:
                if lista2[i] == 0:
                    return suma_bin_aux (lista1,lista2,0,i-1) + [1]
                else:
                    return suma_bin_aux(lista1,lista2,1,i-1) + [0]
            else:
                if lista2[i] == 0:
                    return suma_bin_aux(lista1,lista2,0,i-1) + [0]
                else:
                    return suma_bin_aux(lista1,lista2,0,i-1) + [1]
        else:
             if lista1 [i] ==1:
                if lista2[i] == 0:
                    return suma_bin_aux (lista1,lista2,1,i-1) + [0]
                else:
                    return suma_bin_aux(lista1,lista2,1,i-1) + [1]
             else:
                if lista2[i] == 0:
                    return suma_bin_aux(lista1,lista2,0,i-1) + [1]
                else:
                    return suma_bin_aux(lista1,lista2,1,i-1) + [0]
