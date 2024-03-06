import math
x=float(input("x e deyer verin: "))
eps=0.01
s=0
y=1
a=1
while abs(y)>eps:
    y=((x**a)/a)*((-1)**(a+1))
    a+=1
    s+=y

print(s)