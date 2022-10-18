#LECTURA DE UN ARCHIVO DE TEXTO

def file_read(fname):
    with open(fname, "r") as myfile:
        data = myfile.readlines()
        print(data)


file_read('test.txt')
#Imprime todas las lineas (incluyendo el caracter que identifica que se paso a una nueva linea) en forma de lista