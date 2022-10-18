#ejecucion.py
import os
from estudiante import Estudiante

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
            datos = Estudiante.ingresarDatos()
        elif i == '2':
            os.system('cls')
            datos.imprimirDatos()
            input()
        elif i == '3':
            os.system('cls')
            datos.matricular()
            input()
        elif i == '4':
            os.system('cls')
            datos.pagarPension()
            input()
        else:
            print('\n Opción no valida.')
            input()            

menu()