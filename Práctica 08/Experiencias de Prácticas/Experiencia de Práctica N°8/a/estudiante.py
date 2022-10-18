#estudiante.py
import os

class Estudiante():
    def __new__(clase, nombre):
        print(f' Creando objeto {clase.__name__}')
        objeto = object.__new__(clase)
        return objeto

    def __init__(self, nombre):
        self.nombre = nombre
    
    @classmethod
    def getNombre(self):
        return self.nombre
    def Imprimir(self):
        return '\n### Datos del Estudiante ###\nNombre: {}'.format(self.nombre)

def menu():
    while True:
        os.system('cls')
        print('=========== Sistema de Matricula =============\n')
        print(' 1. Ingresar datos del Estudiante')
        print(' 2. Imprimir datos del Estudiante ')
        i = input('\n Selección:  ')

        if i == '1':
            os.system('cls')
            nombre = input(' Ingresar Nombre: ')
            est = Estudiante(nombre)
            print('\n### Datos del Estudiante registrados correctamente ###')
            input()
        elif i == '2':
            os.system('cls')
            print(est.Imprimir())
            input()
        else:
            print('\n Opción no valida.')
            input()            

menu()