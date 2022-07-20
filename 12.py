print("calculas raices")
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
disc=((b**2)-(4*a*c))
raiz=(disc)**(0.5)

if disc>0:
    x1=((-b)+raiz)/(2*a)
    x2=((-b)-raiz)/(2*a)
    print("x1=",x1)
    print("x2=",x2)
    
elif disc==0:
    x1=((-b)+raiz)/(2*a)
    x2=((-b)-raiz)/(2*a)
    print("x1=",x1)
    print("x2=",x2)
    
else:
    print("las raices son imagi:")
