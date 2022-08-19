#29 Hacer un programa que lea las calificaciones de un alumno en 10 asignaturas, las almacene en un vector
#y calcule e imprima su media, este sistema debe decir si el grupo está en un nivel alto medio o bajo, 
#sabiendo que el un nivel medio esta entre 40% y 70% según la media del grupo

v2 = []
resultado=0
suma=0
nom=(input("Ingrese un nombre: "))
n =int (input(" cuantos notas va a subir  notas de alumno: "))
for i in range(n):
    x = int(input("Ingrese las notas de alumno: "))
    suma=suma+x
   
resultado = suma/n
print(resultado)
