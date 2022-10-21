#! /usr/bin/python3

from anotador import Anotador
from nota import Nota
import datetime

class RepositorioAnotador:
    def __init__(self, archivo = "notas.txt"):
        self.archivo = archivo

    def obtener_todo(self):
        notas = []
        with open(self.archivo, 'r') as fp:
            for nota_como_texto in fp:
                n = self.texto_a_nota(nota_como_texto)
                notas.append(n)
        return notas

    def guardar_todo(self, notas):
        with open(self.archivo, 'w') as fp:
            for nota in notas:
                nota_como_texto = self.nota_a_texto(nota)
                fp.write(nota_como_texto)
            print("Guardado en "+ self.archivo)

    def nota_a_texto(self,nota):
        fc = nota.fecha_creacion
        fecha_en_texto = str(fc.year) + '-' + str(fc.month) + '-' + str(fc.day)
        return nota.texto + ',' + nota.etiquetas + ',' + fecha_en_texto + "\n"

    def texto_a_nota(self, texto):
        texto = texto[:-1] # Sacamos el \n final
        nota_como_lista = texto.split(',')
        n = Nota(nota_como_lista[0], nota_como_lista[1])
        fecha = nota_como_lista[2].split('-')
        n.fecha_creacion = datetime.date(int(fecha[0]),int(fecha[1]),int(fecha[2])) 
        return n
