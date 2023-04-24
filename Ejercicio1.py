#Pide el nombre, apellido y edad del usuario. Después muestra un saludo y su edad dentro de 10 años.

nombre = input("Escribe el nombre: ")
apellido = input("Escribe los apellidos: ")
edad = int(input("Escribe la edad: "))

futuraEdad = edad + 10

print("Hola ", nombre, apellido," ahora tienes ", edad, " y en 10 años tendras ", futuraEdad,)