#estudiante.py
import os

class Estudiante():
    def __init__(self, nombre, dni, carrera, codigo):
        self._nombre = nombre
        self._dni = dni
        self._carrera = carrera
        self._codigo = codigo
    
    @property
    def Nombre(self):
        print('\nObteniendo Nombre...')
        return self._nombre
    
    @property
    def DNI(self):
        print('\nObteniendo DNI...')
        return self._dni

    @property  
    def Carrera(self):
        print('\nObteniendo Carrera...')
        return self._carrera
    
    @property
    def Codigo(self):
        print('\nObteniendo Codigo...')
        return self._codigo

    @Nombre.setter
    def Nombre(self, dato):
        self._nombre = dato

    @DNI.setter
    def DNI(self, dato):
        self._dni = dato
    
    @Carrera.setter
    def Carrera(self, dato):
        self._carrera = dato
    
    @Codigo.setter
    def Codigo(self, dato):
        self._codigo = dato

    

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
            est = Estudiante(nombre, dni, carrera, codigo)
            print('\n### Datos del Estudiante registrados correctamente ###')
            input()
        elif i == '2':
            os.system('cls')
            print(est.Nombre)
            print(est.DNI)
            print(est.Carrera)
            print(est.Codigo)
            input()
        else:
            print('\n Opción no valida.')
            input()            

menu()