from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from modelos.empleado_tiempo_completo import EmpleadoTiempoCompleto
from modelos.empleado_por_horas import EmpleadoPorHoras
from servicios.empresa_servicio import EmpresaServicio
from pydantic import BaseModel

app = FastAPI()
router = APIRouter()


empresa_service = EmpresaServicio()


class EmpleadoTiempoCompletoInput(BaseModel):
    nombre: str
    edad: int
    departamento: str
    anio_contratacion: int
    salario_anual: float

class EmpleadoPorHorasInput(BaseModel):
    nombre: str
    edad: int
    departamento: str
    anio_contratacion: int
    tarifa_hora: float
    horas_trabajadas: int

class DepartamentoInput(BaseModel):
    departamento: str

class TipoEmpleadoInput(BaseModel):
    tipo_empleado: str



@router.post('/modelos/empleado_tiempo_completo')
async def agregar_empleado_tiempo_completo(empleado_data: EmpleadoTiempoCompletoInput):
    empleado = EmpleadoTiempoCompleto(
        nombre=empleado_data.nombre,
        edad=empleado_data.edad,
        departamento=empleado_data.departamento,
        anio_contratacion=empleado_data.anio_contratacion,
        salario_anual=empleado_data.salario_anual
    )
    empresa_service.agregar_empleado(empleado)
    return JSONResponse(content={"message": "Empleado a tiempo completo añadido"}, status_code=201)



@router.post('/modelos/empleado_por_horas')
async def agregar_empleado_por_horas(empleado_data: EmpleadoPorHorasInput):
    empleado = EmpleadoPorHoras(
        nombre=empleado_data.nombre,
        edad=empleado_data.edad,
        departamento=empleado_data.departamento,
        anio_contratacion=empleado_data.anio_contratacion,
        tarifa_hora=empleado_data.tarifa_hora,
        horas_trabajadas=empleado_data.horas_trabajadas
    )
    empresa_service.agregar_empleado(empleado)
    return JSONResponse(content={"message": "Empleado por horas añadido"}, status_code=201)



@router.post('/servicios/empresa_servicio/')
async def consultar_empleados_por_departamento(empleado_data: DepartamentoInput):
    empleados = empresa_service.consultar_empleados_por_departamento(empleado_data.departamento)
    return JSONResponse(content=[empleado.toString() for empleado in empleados])



@router.get('/servicios/empresa_servicio/')
async def consultar_salarios_mensuales():
    salarios = empresa_service.consultar_salarios_mensuales()
    return JSONResponse(content=salarios)



@router.get('/servicios/empresa_servicio/')
async def consultar_empleado_mas_antiguo():
    empleado = empresa_service.consultar_empleado_mas_antiguo()
    if empleado is None:
        raise HTTPException(status_code=404, detail="No hay empleados registrados.")
    return JSONResponse(content=empleado.toString())



@router.post('/servicios/empresa_servicio/')
async def consultar_empleados_por_tipo(empleado_data: TipoEmpleadoInput):
    empleados = empresa_service.consultar_empleados_por_tipo(empleado_data.tipo_empleado)
    return JSONResponse(content=[empleado.toString() for empleado in empleados])


app.include_router(router)


