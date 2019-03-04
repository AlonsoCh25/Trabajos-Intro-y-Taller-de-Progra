def sumalistas(x,y):
    if isinstance (x,list)and (y,list) and len(x)==len(y):
        return sumalistas2(x,y)
    else:
        return "Error de longitud"
def sumalistas2(x,y):
    if x==[1] and y==[]:
        return [1]
    elif x[-1]+y[-1]==2:
        return sumalistas2(x[:-1]+[1],y[:-1])+[0]
    elif x[-1]+y[-1]==3:
        return sumalistas2(x[:-1]+[1],y[:-1])+[1]
    else:
        return sumalistas2(x[:-1],y[:-1])+[1]  

