from modelos.empleado import Empleado

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, edad, departamento, anio_contratacion, tarifa_hora, horas_trabajadas):

        super().__init__(nombre, edad, departamento, anio_contratacion)
        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_mensual(self):
        return self.tarifa_hora * self.horas_trabajadas

    def toString(self):
        base_info = super().toString()
        base_info["salario_mensual"] = self.calcular_salario_mensual()
        return base_info

    def __str__(self):
        return f"{super().__str__()}, Salario por horas={self.calcular_salario_mensual()}"
