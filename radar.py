c= (input("ingrese una palabra:"))
contador=0

for  i in  c :
     contador=contador+1
print(contador)
for  i in  c :
       if i == c[contador-1]:
            contador=contador-1
            ##print(contador)
            if contador==0:
             print("la palbra es palindrome"+c)
       else:
           print("no es palindrome" +c)
           break

 

  
    