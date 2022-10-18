#menu.py
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
            est.ingresarDatos()
        elif i == '2':
            os.system('cls')
            est.imprimirDatos()
            input()
        elif i == '3':
            os.system('cls')
            est.matricular()
            input()
        elif i == '4':
            os.system('cls')
            est.pagarPension()
            input()
        else:
            print('\n Opción no valida.')
            input()

est = Estudiante()
menu()