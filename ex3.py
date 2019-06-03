import blib as bl

x=float(input("Informe o cumprimento do retangulo: "))
y=float(input("Informe a altura do retangulo: "))
z=float(input("Informe a largura do retangulo: "))

h = bl.diag(x,z,y)
print(h)