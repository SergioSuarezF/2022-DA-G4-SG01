#estudiante.py
import os

class Estudiante():
    def __init__(self, nombre, dni, carrera, codigo):
        self.nombre = nombre
        self.dni = dni
        self.carrera = carrera
        self.codigo = codigo
    
    @classmethod
    def getDNI(self):
        return self.dni
    def getNombre(self):
        return self.nombre
    def getCarrera(self):
        return self.carrera
    def getCodigo(self):
        return self.codigo
    
    @staticmethod
    def IngresarDatos():
        return '\n### Datos del Estudiante registrados correctamente ###'

    @staticmethod
    def ImprimirDatos(nombre, dni, carrera, codigo):
        return '\n### Datos del Estudiante ###\nNombre: {}\nDNI: {}\nCarrera: {}\nCodigo: {}'.format(nombre, dni, carrera, codigo)
    
    

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
            dni = input(' Ingresar DNI: ')
            carrera = input(' Ingresar Carrera: ')
            codigo = input(' Ingresar Codigo: ')
            print(Estudiante.IngresarDatos())
            input()
        elif i == '2':
            os.system('cls')
            print(Estudiante.ImprimirDatos(nombre, dni, carrera, codigo))
            input()
        else:
            print('\n Opción no valida.')
            input()            

menu()