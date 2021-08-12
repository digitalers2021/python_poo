

asignaciones = {}

lista_alumnos = ["pepe", "juana", 'adrian']

materias = ["python", "javascript"]

def asignar_materia(alumno, materia):
    asignaciones.update({alumno: materia})

asignar_materia(lista_alumnos[0], materias[0])
print(asignaciones)
