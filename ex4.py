from random import choice

x = ["fala", "cachorro", "esperado", "cadela", "macho", "carreta", "furacao"]
y=[]
let=[]
rd = choice(x)
tentativas =[]
letras =0

for i in (rd):
    y.append("_")
    let.append(i)
print(y)
print(let)

cont=0
w=[]
tent=0

while(tent < 5 and letras < len(rd)):
    resp = input("Informe uma letra ou um palpite: ")
    if(len(resp)==1):
        tent += 1
        if(resp in rd and (resp not in tentativas)):
            for (pos,letra) in enumerate(rd):
                if(letra == resp):
                    w.append(letra)
                    y[pos] = resp.upper()
                    letras += 1
                    tentativas.append(resp)
                    y[pos] = letra
            print(y)
            if(y==w):
                print("Voce acertou.")

    elif(len(resp)>1):
        tent+=5
        if(resp==rd):
            print("Parabés você acertou!!!!!!!!! S2")
        else:
            print("Voce morreu.")








    
    