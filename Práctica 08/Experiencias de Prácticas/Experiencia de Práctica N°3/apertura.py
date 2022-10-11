#ABRIR UN ARCHIVO PARA ESCRITURA
archivo = open('TipoTexto.txt','r')
imprimir = archivo.read()
print(imprimir)
archivo.close()