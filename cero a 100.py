# Introducir dos números por teclado que estén entre los 100 números enteros. Imprimir
# y Almacenar los números naturales que hay entre ambos números
#empezando por el más pequeño, contar cuantos hay y cuántos de ellos son pares.
# Calcular la suma de los impares.
n1=int(input("ingresar un numero de 1 al 100:"))
n2=int(input("ingresar un numero de 1 al 100:"))
for i in range (0,100):  
    n1=n1+1
    n2=n2+1
    if n1 % 2 ==0:     
        print("paraes",n1)      
    if n2 % 2 !=0:     
        print("impares",n2)