class Sumalos:
    def __init__(self):
        pass
    def SumadeBases(self,num,num2,base,acarreo):
        if isinstance (num,list) and (num2,list) and (base,int) and (acarreo,int) and len(num)==len(num2):
            return self.SumadeBases2(num,num2,base,acarreo)
        else:
            return "Error"
    def SumadeBases2(self,num,num2,base,acarreo):
        if num==[] and num2==[] and acarreo>=0 and base>=0:
            return [acarreo]
        elif (num[-1]+num2[-1]+acarreo)>base:
            return self.SumadeBases2(num[:-1],num2[:-1],base,1)+([(num[-1]+num2[-1]+acarreo)%base])
        elif (num[-1]+num2[-1]+acarreo)==base:
            return self.SumadeBases2(num[:-1],num2[:-1],base,1)+[0]
        else:
            return self.SumadeBases2(num[:-1],num2[:-1],base,0)+[num[-1]+num2[-1]+acarreo]

