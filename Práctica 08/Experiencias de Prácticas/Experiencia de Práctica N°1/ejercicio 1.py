mayor = 0
menor = 9999999999999999
lista = []
for a in range(0,6):
   i = int(input("Ingrese un numero:" ))
   while i in lista:
      i = int(input("Ingrese un numero:" ))
   lista.append(i)
   if (i > mayor):
      mayor = i
   if (i < menor):
      menor = i
print("El elemento en la posicion 3 es: ", lista[2])
print("El elemento en la posicion 4 es: ", lista[3])
print("El numero mayor es: ", mayor)
print("El numero menor es: ", menor)




