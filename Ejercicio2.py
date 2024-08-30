from datetime import date

class RegistroAsistencia:
    def __init__(self, fecha, estado, razon=None):
        # Inicializa un registro de asistencia con fecha, estado y razón (opcional).
        self.fecha = fecha
        self.estado = estado
        self.razon = razon

    def __str__(self):
        # Devuelve una representación en cadena del registro de asistencia.
        if self.estado == 'Permiso':
            return f"Fecha: {self.fecha}, Estado: {self.estado}, Razón: {self.razon}"
        return f"Fecha: {self.fecha}, Estado: {self.estado}"
    
class Estudiante:
    def __init__(self, nombre):
        # Inicializa un estudiante con nombre y una lista de registros de asistencia.
        self.nombre = nombre
        self.registros = []

    def agregar_asistencia(self, fecha, estado, razon=None):
        # Agrega un registro de asistencia al estudiante.
        self.registros.append(RegistroAsistencia(fecha, estado, razon))

    def __str__(self):
        # Devuelve una representación en cadena del estudiante y sus registros.
        registros_str = ', '.join(str(registro) for registro in self.registros)
        return f"Estudiante: {self.nombre}, Registros: {registros_str}"

class Docente:
    def __init__(self, nombre):
        # Inicializa un docente con nombre y un listado de estudiantes.
        self.nombre = nombre
        self.estudiantes = {}

    def agregar_estudiante(self, estudiante):
        # Agrega un estudiante al listado del docente.
        self.estudiantes[estudiante.nombre] = estudiante

    def registrar_asistencia(self, nombre_estudiante, fecha, estado, razon=None):
        # Registra la asistencia de un estudiante.
        if nombre_estudiante in self.estudiantes:
            self.estudiantes[nombre_estudiante].agregar_asistencia(fecha, estado, razon)
        else:
            print("Estudiante no encontrado.")

    def mostrar_asistencia(self):
        # Muestra la asistencia de todos los estudiantes del docente.
        for estudiante in self.estudiantes.values():
            print(estudiante)

class Director:
    def __init__(self):
        # Inicializa el director con una lista de docentes.
        self.docentes = []

    def agregar_docente(self, docente):
        # Agrega un docente a la lista del director.
        self.docentes.append(docente)

    def mostrar_asistencia_total(self):
        # Muestra la asistencia de todos los estudiantes de todos los docentes.
        for docente in self.docentes:
            print(f"Docente: {docente.nombre}")
            docente.mostrar_asistencia()

# Ejemplo de uso
estudiante1 = Estudiante("Mario Antonio")
estudiante2 = Estudiante("Jose Medrano")

docente = Docente("Ing. Wilian")
docente.agregar_estudiante(estudiante1)
docente.agregar_estudiante(estudiante2)

# Registrar asistencia
docente.registrar_asistencia("Mario Antonio", date.today(), "Presente")
docente.registrar_asistencia("Jose Medrano", date.today(), "Permiso", "Cita médica")
print("-------------------------------------------------------------------------------------")
# Mostrar asistencia
director = Director()
director.agregar_docente(docente)
print("Asistencia total:")
director.mostrar_asistencia_total()