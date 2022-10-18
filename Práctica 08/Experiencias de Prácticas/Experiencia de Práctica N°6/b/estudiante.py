#estudiante.py
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
        return datos
    
    def imprimirDatos(datos):
        check = input('\n Ingresar DNI del Estudiante: ')
        if (check == datos.dni):
            print('\n### Datos del Estudiante ###\nNombre: {}\nDNI: {}\nFecha de Nacimiento: {}'.format(datos.nombre, datos.dni, datos.fnacimiento))
        else:
            print('\n### Estudiante no existente ###')

    def matricular(datos):
        check = input('\n Ingresar DNI del Estudiante: ')
        if (check == datos.dni):
            datos.carrera = input(' Ingresar Carrera: ')
            datos.codigo = ('2022' + ''.join(random.choices(string.digits, k=6)))
            print('\n### Matricula Exitosa ###\nCarrera:', datos.carrera, '\nCodigo del Estudiante:', datos.codigo)
        else:
            print('\n### Estudiante no existente ###')        

    def pagarPension(datos):
        check = input('\n Ingresar Codigo de Estudiante: ')
        if (check == datos.codigo):
            print('\n### Pago Exitoso! ###')
        else:
            print('\n### Codigo no existente ###')