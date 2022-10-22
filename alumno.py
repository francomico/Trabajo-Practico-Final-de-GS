import datetime
ultima_id = 0
class Alumno:
    #Datos del alumno
    def __init__(self, nombre, apellido, nivel, grado):
        self.nombre = nombre
        self.apellido = apellido
        self.nivel = nivel
        self.grado = grado
        self.fecha_creacion = datetime.date.today()
        global ultima_id
        ultima_id += 1
        self.id = ultima_id


    #Metodo para buscar por nombre y apellido
    def coincide(self, nombre_apellido_buscar):
        if nombre_apellido_buscar in self.nombre + ' ' + self.apellido:
            return True
        else:
            return False
    
    #Metodo que determina si el alumno coincide con el filtro de búsqueda. Retorna True si es así y False de lo contrario
    def coincide_filtro(self, filtro):
        return (filtro in self.nivel) or (filtro in self.grado) or (filtro in self.nombre) or (filtro in self.apellido)