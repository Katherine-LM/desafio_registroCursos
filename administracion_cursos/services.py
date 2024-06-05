from model import Curso, Profesor, Estudiante, Direccion

def crear_curso(nombre, descripcion):
    return Curso(nombre, descripcion)

def crear_profesor(nombre, especialidad):
    return Profesor(nombre, especialidad)

def crear_estudiante(nombre, direccion):
    return Estudiante(nombre, direccion)

def crear_direccion(calle, ciudad, pais):
    return Direccion(calle, ciudad, pais)

def obtiene_estudiante(estudiante):
    return estudiante

def obtiene_profesor(profesor):
    return profesor

def obtiene_curso(curso):
    return curso

def agrega_profesor_a_curso(profesor, curso):
    curso.profesores.append(profesor)

def agrega_cursos_a_estudiante(estudiante, cursos):
    estudiante.cursos.extend(cursos)

def imprime_estudiante_cursos(estudiante):
    print(f"Cursos de {estudiante.nombre}:")
    for curso in estudiante.cursos:
        print(f"- {curso.nombre}: {curso.descripcion}")
