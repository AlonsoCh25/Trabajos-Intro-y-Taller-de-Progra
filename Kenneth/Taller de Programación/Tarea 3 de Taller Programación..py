#Tarea #3 Taller de progra, utilizar una clase, que
#realice la resta de un número de cualquier base.
class restas(object):
    def __int__(self):
        pass
    def rest(self, num1, num2):
        if (isinstance (num1, list) and isinstance (num2, list)
        and len(num1)==len(num2)):
            return self.rest_aux(num1, num1, num2)
        else: return "Los valores nu cumplen con las condiciones"

    def rest_aux(self, num1, prest, num2):
        if num1 == []:
            return []
        if ((num1[-1]) - (num2[-1])) >= 0:
            return self.rest_aux(num1[:-1],prest[:-1], num2[:-1]) + [(num1[-1]) - (num2[-1])]   
        if ((prest[-1]) - (num2[-1])) < 0:
            return self.rest_aux(num1[-2]-1, prest[-1]+1, num2)
