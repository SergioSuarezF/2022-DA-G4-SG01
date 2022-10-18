#LECTURA DE UN ARCHIVO DE TEXTO

def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)


file_read_from_head('test.txt', 2)
#Imprime agunas lineas del archivo pero no todas de acuerdo al parametro que se envia