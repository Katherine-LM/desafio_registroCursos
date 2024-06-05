class Curso:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.profesores = []
        self.estudiantes = []

class Profesor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

class Estudiante:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.cursos = []

class Direccion:
    def __init__(self, calle, ciudad, pais):
        self.calle = calle
        self.ciudad = ciudad
        self.pais = pais
