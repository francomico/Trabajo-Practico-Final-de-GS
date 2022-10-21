class Alumno:
    #Datos del alumno
    def __init__(self, nombre, apellido, nivel, grado, asistencia):
        self.nombre = nombre
        self.apellido = apellido
        self.nivel = nivel
        self.grado = grado
        self.asistencia = asistencia

    #Metodo para calcular la asistencia del alumno
    def calcular_asistencia(self):
        if self.asistencia >= 75:
            return "El alumno es regular"
        else:
            "El alumno es no regular"



    #Metodo para buscar por nombre y apellido
    def coincide(self, nombre_apellido_buscar):
        if nombre_apellido_buscar in un_alumno.nombre or nombre_apellido_buscar in un_alumno.apellido:
            return True
        else:
            return False
    
    #Metodo que determina si el alumno coincide con el filtro de búsqueda. Retorna True si es así y False de lo contrario
    def coincide_filtro(self, filtro):
        return (filtro in self.nivel) or (filtro in self.grado) or (filtro in self.asistencia) or (filtro in self.nombre) or (filtro in self.apellido)
