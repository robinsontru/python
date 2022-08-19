numero=int(input("ingresar un numero:"))
numero1=int(input("ingresar un numero:"))
num=([i for i in range (numero,numero1)])
print(num)
numero2=int(input("¿que digito quieres tomar?"))
if numero2<=numero1:
    buscar=num.index(numero2)
    print("la posicion de el vector es ",num, "=",buscar)
else:
    print("la posicion de el vector es ",num, "no se encuentro el vector")

