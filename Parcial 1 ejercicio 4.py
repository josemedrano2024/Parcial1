from datetime import date

class Empleado:
    def __init__(self, nombre, anio_ingreso):
        self.nombre = nombre
        self.anio_ingreso = anio_ingreso

    def calcular_antiguedad(self):
        return date.today().year - self.anio_ingreso

    def calcular_bono(self):
        if self.calcular_antiguedad() > 5:
            return 100  # Bono adicional por más de 5 años de servicio
        return 0

    def calcular_pago(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")


class EmpleadoPlazaFija(Empleado):
    def __init__(self, nombre, anio_ingreso, salario_base, comisiones):
        super().__init__(nombre, anio_ingreso)
        self.salario_base = salario_base
        self.comisiones = comisiones

    def calcular_pago(self):
        return self.salario_base + self.comisiones + self.calcular_bono()


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, anio_ingreso, horas_trabajadas, tarifa_hora):
        super().__init__(nombre, anio_ingreso)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora

    def calcular_pago(self):
        return self.horas_trabajadas * self.tarifa_hora + self.calcular_bono()


def generar_planilla(empleados):
    print("\n--- Planilla de Pago ---")
    for empleado in empleados:
        pago_total = empleado.calcular_pago()
        print(f"Empleado: {empleado.nombre}, Pago Total: ${pago_total}")

# Ejemplo de uso
empleados = [
    EmpleadoPlazaFija("Carlos", 2010, 1200, 300),
    EmpleadoPlazaFija("Ana", 2020, 1000, 200),
    EmpleadoPorHoras("Luis", 2018, 160, 10),
    EmpleadoPorHoras("Maria", 2014, 200, 12)
]

generar_planilla(empleados)
