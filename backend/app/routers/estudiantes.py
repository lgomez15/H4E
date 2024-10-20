from fastapi import APIRouter

router = APIRouter(
    prefix="/estudiantes",
    tags=["estudiantes"],
)

@router.get("/")
def listar_estudiantes():
    # TODO: Implementar lógica para listar estudiantes
    pass

@router.get("/{estudiante_id}")
def obtener_estudiante(estudiante_id: int):
    # TODO: Implementar lógica para obtener datos de un estudiante
    pass

@router.post("/")
def crear_estudiante():
    # TODO: Implementar lógica para crear un nuevo estudiante
    pass

@router.put("/{estudiante_id}")
def actualizar_estudiante(estudiante_id: int):
    # TODO: Implementar lógica para actualizar un estudiante
    pass

@router.delete("/{estudiante_id}")
def eliminar_estudiante(estudiante_id: int):
    # TODO: Implementar lógica para eliminar un estudiante
    pass
