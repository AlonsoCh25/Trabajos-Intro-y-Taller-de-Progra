import math
class Medias:
    def __init__(self):
        pass
    def MediaGeo(self,lista):
        if  isinstance (lista,list) and len(lista)>0:
            return self.Media(lista)**(1/len(lista), self.Media(lista))
        else:
            return "Error la lista no es lo suficientemente grande"
    def Media(self,lista):
        if lista==[]:
            return []
        else:
            return lista[0]* self.Media(lista[1:])

