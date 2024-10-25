
#inicia clase de empleado, en "class" creamos un "modelo" o figura
class Empleado:
    def __init__(self, nombre: str, edad: int, departamento: str, anio_contratacion: int):#puedes entrar y modificar los atributos de la instancia actual
        self.nombre = nombre#es un atributo de la instancia de empleado
        self.edad = edad
        self.departamento = departamento
        self.anio_contratacion = anio_contratacion

    def get_nombre(self) -> str:#le asignamos a nombre un tipo string que esto significa una cadena de caracteres
        return self.nombre#"retornamos" la variable "nombre" retorna significa que esta linea de codigo se encarga de dar el nombre

    def get_edad(self) -> int:#le asignamos a edad un tipo int que esto son numeros enteros, o sea 0 y no 0.0
        return self.edad#"retornamos" la variable "edad"  esta linea se encarga de dar la edad de "empleado"

    def get_departamento(self) -> str:
        return self.departamento

    def get_anio_contratacion(self) -> int:
        return self.anio_contratacion

    def calcular_antiguedad(self) -> int:
        return 2024 - self.anio_contratacion

    def toString(self):
        return {
            "nombre": self.nombre, #toString este método se utiliza para definir la forma de cadena de un objeto
            "edad": self.edad,
            "departamento": self.departamento,
            "anio_contratacion": self.anio_contratacion,
            "antiguedad": self.calcular_antiguedad()
        }

    def __str__(self):
        return f"Empleado{{nombre='{self.nombre}', edad={self.edad}, departamento='{self.departamento}', antigüedad={self.calcular_antiguedad()}}}"
