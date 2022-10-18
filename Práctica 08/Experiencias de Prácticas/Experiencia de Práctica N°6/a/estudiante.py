#estudiante.py
import string
import random

class Estudiante:
    nombre = ''
    dni = ''
    fnacimiento = ''
    carrera = ''
    codigo = ''

    def ingresarDatos(self):
        self.nombre = input(' Ingresar Nombre: ')
        self.dni = input(' Ingresar DNI: ')
        self.fnacimiento = input(' Ingresar Fecha de Nacimiento: ')
        input(print('\n### Datos del Estudiante registrados correctamente ###'))
    
    def imprimirDatos(self):
        check = input('\n Ingresar DNI del Estudiante: ')
        if (check == self.dni):
            print('\n### Datos del Estudiante ###\nNombre:', self.nombre, '\nDNI:', self.dni, '\nFecha de Nacimiento:', self.fnacimiento)
        else:
            print('\n### Estudiante no existente ###')  

    def matricular(self):
        check = input('\n Ingresar DNI del Estudiante: ')
        if (check == self.dni):
            self.carrera = input(' Ingresar Carrera: ')
            self.codigo = ('2022' + ''.join(random.choices(string.digits, k=6)))
            print('\n### Matricula Exitosa ###\nCarrera:', self.carrera, '\nCodigo del Estudiante:', self.codigo)
        else:
            print('\n### Estudiante no existente ###')        

    def pagarPension(self):
        check = input('\n Ingresar Codigo de Estudiante: ')
        if (check == self.codigo):
            print('\n### Pago Exitoso! ###')
        else:
            print('\n### Codigo no existente ###')