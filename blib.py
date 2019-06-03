def salliquido(salb):
    res=0
    if(salb<=1751.81):
        res = salb*0.92
    elif(salb<=2919.72):
        res = salb*0.91
    elif(salb<=5893.45):
        res = salb*0.89
    elif(salb>5893.45):
        res = salb-642.34
    if(res>1903.99 and res<=2826.65):
        res = res - ((res*0.075) - 142.8)
    elif(res>2826.65 and res <= 3751.05):
        res = res - ((res*0.15) - 354.8)
    elif(res>3751.5 and res<=4664.68):
        res = res- (res*0.225-636.13)
    elif(res>4664.68):
        res = res- (res*0.27-869.36)
    return res

def calcav(xx,y):
    x=[]

    if(xx-2>=1):
        if(y+1<=8):
            x.append((xx-2,y+1))
        if(y-1>=1):
            x.append(((xx-2,y-1)))
    if(xx+2<=8):
        if(y+1<=8):
            x.append((xx+2,y+1))
        if(y-1>=1):
            x.append((xx+2,y-1))
    if(y-2>=1):
        if(xx-1>=1):
            x.append((xx-1,y-2))
        if(xx+1<=8):
            x.append((xx+1,y-2))
    if(y+2<=8):
        if(xx-1>=1):
            x.append((xx-1,y+2))
        if(xx+1<=8):
            x.append((xx+1,y+2))
    return x

def diag(x,z, y):
    d = (x**2 + z**2) ** 0.5
    df = (d**2 + y**2) ** 0.5
    return df


