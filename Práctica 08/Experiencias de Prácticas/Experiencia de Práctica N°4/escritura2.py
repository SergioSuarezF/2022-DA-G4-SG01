#ESCRIBIR EN UN ARCHIVO

#Se crea una funcion que requiere una variable
def file_read(fname):
    #Abre y escribe en un archivo de texto
    with open(fname, "w") as myfile:
        #Añade 2 lineas de texto
        myfile.write("Ejercicios Python\n")
        myfile.write("Ejercicios Java")
    #Vuelve a abrir el archivo para imprimir las lineas escritas
    txt = open(fname)
    print(txt.read())


file_read('abc.txt')