#LECTURA DE UN ARCHIVO DE TEXTO
def file_read(fname):
    txt = open(fname)
    print(txt.read())


file_read('test.txt')