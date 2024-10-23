

class Empleado:
    def __init__(self, nombre: str, edad: int, departamento: str, anio_contratacion: int):
        self.nombre = nombre
        self.edad = edad
        self.departamento = departamento
        self.anio_contratacion = anio_contratacion

    def get_nombre(self) -> str:
        return self.nombre

    def get_edad(self) -> int:
        return self.edad

    def get_departamento(self) -> str:
        return self.departamento

    def get_anio_contratacion(self) -> int:
        return self.anio_contratacion

    def calcular_antiguedad(self) -> int:
        return 2024 - self.anio_contratacion

    def toString(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "departamento": self.departamento,
            "anio_contratacion": self.anio_contratacion,
            "antiguedad": self.calcular_antiguedad()
        }

    def __str__(self):
        return f"Empleado{{nombre='{self.nombre}', edad={self.edad}, departamento='{self.departamento}', antigüedad={self.calcular_antiguedad()}}}"
