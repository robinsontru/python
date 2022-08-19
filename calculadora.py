#Crea un programa llamado calculadora que permita emplear por mediio de funciones sumar,
# restar, multiplicar y dividir 2 numeros, el programa debe darle la posibilidad de seleccionar 
# la operacion que quiere hacer hasta que el usuario seleccione la opcion de salir del programa
n1 = int(input("Introduce tu primer número: ") )
n2 = int(input("Introduce tu segundo número: ") )

opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) divicion
    5) Apagar calculadora
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
    elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta de",n1,"-",n2,"es igual a",n1-n2)
    elif opcion == 3:
        print(" ")
        print("RESULTADO: El producto de",n1,"*",n2,"es igual a",n1*n2)
    elif opcion == 4:
         print(" ")
         print("RESULTADO: El producto de",n1,"/",n2,"es igual a",n1/n2)
    break



     








