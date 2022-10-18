#Elaborar Funciones que reciban diccionarios como parámetros para procesar Datos.
Empleado = {
'Nombre' : 'Margarita',
'Edad' : 55,
'Genero' : 'Femenino'
}

Cliente = {
'Nombre' : 'Margarita',
'Apellido' : 'Filosa',
'Alias' : 'Cuchillos',
'Padres' : ["Maria Chaira", "Carlos Cortez"], 
'Edad' : 55,
'Genero' : 'Femenino',
'Estado Civil' : 'Soltera',
'Hijos' : 'Ninguno/a',
'Mascotas' : 'Gatos',
'Nombres de mascotas' : ["Mango", "Doble Filo"] 
}

print("Elaborar Funciones que reciban diccionarios como parámetros para procesar Datos.")

print("El empleado ",Empleado['Nombre']," de género ",Empleado['Genero']," tiene ",Empleado['Edad']," años ")

print("Los padres del Cliente son: ")
print(Cliente['Padres'])

#Agregar Funciones con parámetros por defecto.
def areaTri (a, b, c=2):
    rpta = (a * b)/c
    return rpta

print("")
print("Agregar Funciones con parámetros por defecto.")

print("El área del triángulo es:")
print(areaTri(5,9))#falta el parámetro por defecto

#Agregar Funciones que te vuelva más de un valor de retorno.
def mcmYmcd(n1, n2):
    op1 = mcm(n1, n2)
    op2 = mcd(n1, n2)
    return op1, op2


def mcm(a, b):
    return(a*b)/mcd(a,b)

def mcd(a, b):
    temp = 0
    while b!=0:
        temp = b
        b = a % b
        a = temp
    return a

print("")
print("Agregar Funciones que te vuelva más de un valor de retorno.")

print(mcmYmcd(90,45))
x, y = mcmYmcd(90,45)
print(x)
print(y)

lista = mcmYmcd(20,8)
print(lista)



































