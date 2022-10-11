#ESCRIBIR EN UN ARCHIVO
def file_read(fname):
    with open(fname, "w") as myfile:
        myfile.write("Ejercicios Python\n")
        myfile.write("Ejercicios Java")
    txt = open(fname)
    print(txt.read())


file_read('abc.txt')