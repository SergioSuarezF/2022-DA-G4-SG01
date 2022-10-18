#ejecucion2.py
import os
import string
import random

class Estudiante():
    def __init__(self, nombre, dni, fnacimiento, carrera, codigo):
        self.nombre = nombre
        self.dni = dni
        self.fnacimiento = fnacimiento
        self.carrera = carrera
        self.codigo = codigo

    def ingresarDatos():
        nombre = input(' Ingresar Nombre: ')
        dni = input(' Ingresar DNI: ')
        fnacimiento = input(' Ingresar Fecha de Nacimiento: ')        
        datos = Estudiante(nombre, dni, fnacimiento, '', '')
        input(print('\n### Datos del Estudiante registrados correctamente ###'))
        Estudiantes.append(datos)
    
    def imprimirDatos(datos):
        print('\n### Datos del Estudiante ###\nNombre: {}\nDNI: {}\nFecha de Nacimiento: {}'.format(datos.nombre, datos.dni, datos.fnacimiento))
    
    def matricular():
        check = input('\n Ingresar DNI del Estudiante: ')
        for datos in Estudiantes:
            if (check == datos.dni):
                datos.carrera = input(' Ingresar Carrera: ')
                datos.codigo = ('2022' + ''.join(random.choices(string.digits, k=6)))
                print('\n### Matricula Exitosa ###\nCarrera:', datos.carrera, '\nCodigo del Estudiante:', datos.codigo)
            else:
                print('\n### Estudiante no existente ###')
           
    def pagarPension():
        check = input('\n Ingresar Codigo de Estudiante: ')
        for datos in Estudiantes:
            if (check == datos.codigo):
                print('\n### Pago Exitoso! ###')
            else:
                print('\n### Codigo no existente ###')
        
    def imprimir():
        for datos in Estudiantes:
            datos.imprimirDatos()


def menu():
    while True:
        os.system('cls')
        print('=========== Sistema de Matricula =============\n')
        print(' 1. Ingresar datos del Estudiante')
        print(' 2. Imprimir datos del Estudiante ')
        print(' 3. Matricular Estudiante')
        print(' 4. Pago de Pensiones')
        i = input('\n Selección:  ')

        if i == '1':
            os.system('cls')
            Estudiante.ingresarDatos()
        elif i == '2':
            os.system('cls')
            Estudiante.imprimir()
            input()
        elif i == '3':
            os.system('cls')
            Estudiante.matricular()
            input()
        elif i == '4':
            os.system('cls')
            Estudiante.pagarPension()
            input()
        else:
            print('\n Opción no valida.')
            input()            

Estudiantes = []
menu()