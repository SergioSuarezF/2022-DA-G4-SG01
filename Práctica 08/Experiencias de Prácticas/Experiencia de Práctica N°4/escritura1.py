# ESCRIBIR UN ARCHIVO DE TEXTO

archivo = open('Escritura.txt', 'w')
num = int(input('Ingresar numero de lineas: '))
i = 0
while i < num:
    data = input('Ingresar linea de texto: ')
    archivo.write(data + '\n')
    i += 1
archivo.close()
