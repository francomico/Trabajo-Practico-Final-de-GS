#! /usr/bin/env python3
from alumnado import Alumnado
import sys
class Menu:
    '''Mostrar un menú y responder a las opciones'''
    def __init__(self):
        self.alumnado = Alumnado()
        self.opciones= {
            "1": self.mostrar_alumno,
            "2": self.buscar_alumno,
            "3": self.agregar_alumno,
            "4": self.modificar_alumno,
            "5": self.salir
        }

    def mostrar_menu(self):
        print("""
Menú del anotador:
1. Mostrar todos los alumnos
2. Buscar Alumnos
3. Agregar alumno
4. Modificar alumno
5. Salir
""")

    def ejecutar(self):
        '''Mostrar el menu y responder a las opciones.'''
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opción válida".format(opcion))

    def mostrar_alumno(self, alumnos=None):
        if not alumnos:
            alumnos = self.alumnado.alumnos
        for alumno in alumnos:
            print("{0}: {1}\n{2}".format(alumnos.buscar_por_nombre_apellido, alumnos.nivel, alumnos.grado))
    
    def buscar_alumno(self):
        filtro = input("Buscar: ")
        alumnos = self.alumnado.buscar(filtro)
        if alumnos:
            self.mostrar_alumno(alumnos)
        else:
            print("Ninguna nota coincide con la búsqueda")
    
    def agregar_alumno(self):
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno")
        nivel = input("Ingrese el nivel del alumno")
        grado = input("Ingrese el grado del alumno")
        self.alumnado.nuevo_alumno(nombre)
        self.alumnado.nuevo_alumno(apellido)
        self.alumnado.nuevo_alumno(nivel)
        self.alumnado.nuevo_alumno(grado)
        print("Su alumno ha sido agregado.")

    def modificar_alumno(self):
        identificador = input("Ingrese el nombre o el apellido del alumno a modificar: ")
        nivel = input("Ingrese el nivel del alumno: ")
        grado = input("Ingrese el grado del alumno: ")
        if nivel:
            self.alumnado.modificar_alumno(identificador, nivel)
        if grado:
            self.alumnado.modificar_etiquetas(identificador, grado)
    
    def salir(self):
        print("Gracias por utilizar el sistema.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().ejecutar()