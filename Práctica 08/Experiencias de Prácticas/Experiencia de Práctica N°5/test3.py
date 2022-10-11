#LECTURA DE UN ARCHIVO DE TEXTO
def file_read(fname):
    with open(fname, "r") as myfile:
        data = myfile.readlines()
        print(data)


file_read('test.txt')
