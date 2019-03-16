import math
class media:
    def _init_(self):
        pass
    def mediageometrica(self, lista):
        if isinstance(lista, list) and (len(lista)>0):
            return self.media_aux(lista)**(1/len(lista)), self.media_aux(lista)//10 
        else: return "Con los valores ingresados no se puede realizar una media geométrica"
    def media_aux(self, lista):
        if (lista == []):
            return []
        else:
            return lista [0] * media_aux(lista[1:])
