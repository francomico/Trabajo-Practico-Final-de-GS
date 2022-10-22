#! /usr/bin/python3

from alumnado import Alumnado
from alumno import Alumno
import datetime

class RepositorioAlumnado:
    def __init__(self, archivo = "notas.txt"):
        self.archivo = archivo

    def obtener_todo(self):
        alumnos = []
        with open(self.archivo, 'r') as archivo_alumno:
            for alumnos_texto in archivo_alumno:
                n = self.texto_a_alumno(alumnos_texto)
                alumnos.append(n)
        return alumnos

    def guardar_todo(self, alumnos):
        with open(self.archivo, 'w') as archivo_alumno:
            for alumno in alumnos:
                alumnos_texto = self.alumno_a_texto(alumno)
                archivo_alumno.write(alumnos_texto)
            print("Guardado en "+ self.archivo)

    def alumno_a_texto(self, alumno):
        fc = alumno.fecha_creacion
        fecha_en_texto = str(fc.year) + '-' + str(fc.month) + '-' + str(fc.day)
        return alumno.nombre + ',' + alumno.apellido + ',' + alumno.nivel + ',' + alumno.grado + ',' + alumno.asistencia + fecha_en_texto + "\n"

    def texto_a_alumno(self, texto):
        texto = texto[:-1] # Sacamos el \n final
        alumno_como_lista = texto.split(',')
        n = Alumno(alumno_como_lista[0], alumno_como_lista[1])
        fecha = alumno_como_lista[2].split('-')
        n.fecha_creacion = datetime.date(int(fecha[0]),int(fecha[1]),int(fecha[2])) 
        return n