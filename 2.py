##segundo
num1=0
num2=0

num1=int((input("ingresa un numero a:")))
num2=int((input("ingresa un numero b:")))
i=1
mxd=1
while (i<=9) :
       if(num1%i==0 and num2%i==0 ):
            mxd=mxd*i 
            num1=num1//i
            num2=num2//i
       i=i+1    
print("el maximo comun divisor es ",mxd)


