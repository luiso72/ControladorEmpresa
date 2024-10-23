from modelos.empleado import Empleado


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, edad, departamento, anio_contratacion, salario_anual):
        super().__init__(nombre, edad, departamento, anio_contratacion)
        self.salario_anual = salario_anual

    def calcular_salario_mensual(self):
        return self.salario_anual / 12

    def toString(self):
        base_info = super().toString()
        base_info["salario_mensual"] = self.calcular_salario_mensual()
        return base_info

    def __str__(self):
        return f"{super().__str__()}, Salario mensual={self.calcular_salario_mensual()}"
