def sumalistas(x,y,z):
    if isinstance (x,list)and (y,list) and len(x)==len(y) and (z,list):
        return sumalistas2(x,y,z)
    else:
        return "Error de longitud"
def sumalistas2(x,y,z):
    if x==[] and y==[]:
        return []
    elif x[-1]+y[-1]==2:
        return sumalistas2(x[:-1]+[1],y[:-1],z+[1])+[0]
    elif x[-1]+y[-1]==3:
        return sumalistas2(x[:-1]+[1],y[:-1],z+[1])+[1]
    else:
        return sumalistas2(x[:-1],y[:-1],z)+[1]  

