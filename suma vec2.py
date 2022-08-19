num1=[1,2,3,4,5,5,6,8,8,8,8,]
num2=[1,8,8,7,7,7,7,75,5,5,]
suma=0
resultado=0
suma2=0
for i in range(num1):
  
    suma=suma+num1
    print(suma)
print()
for i in range(num2):
      
      resultado=resultado+num2
      print(resultado)
print()
suma2=suma2+suma+resultado

print(f"({num1}+{num2}={suma2})",end=" ")
