#LECTURA DE UN ARCHIVO DE TEXTO

import glob
char_list = []
files_list = glob.glob("*.txt")
for file_elem in files_list:
    with open(file_elem, "r") as f:
        char_list.append(f.read())
print(char_list)
#Imprime las lineas de cada uno de los archivos de texto que se encuentren en el directorio en una lista