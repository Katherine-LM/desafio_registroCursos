from model import Curso, Profesor, Estudiante, Direccion
from services import *

# Aquí puedes escribir pruebas para tus funciones
curso = crear_curso("Matemáticas", "Curso de matemáticas avanzadas")
assert curso.nombre == "Matemáticas"
assert curso.descripcion == "Curso de matemáticas avanzadas"

profesor = crear_profesor("Juan", "Matemáticas")
assert profesor.nombre == "Juan"
assert profesor.especialidad == "Matemáticas"
