from typing import Annotated, List

from fastapi import APIRouter, Path, Query

from server.schemas.expedientes_schemas import NewRecordRequest, RecordResponse, RecordRequest
from server.controller import ExpedientesController
from server.exceptions import InternalServerError, NotFound

router = APIRouter(prefix='/expedientes')
router.responses = {
    500: InternalServerError.as_dict(),
}
controller = ExpedientesController()

@router.post(
    '',
    status_code=201,
    responses={
        201: {'description': 'Expediente creado'}
    },
    description='Crea un expediente nuevo con los campos pasado por Body Param. Falla si faltan alguno de los campos obligatorios.'
    )  # POST /expedientes
async def create(new_record: NewRecordRequest) -> RecordResponse:
    return controller.create(new_record)

@router.get(
    '',
    status_code=200,
    responses={
        200: {'description': 'Listado de expediente'}
    },
    description='Retorna una lista paginada con los expedientes. Si no hay expedientes para mostrar, retorna lista vacía.'
    )  # POST /expedientes
async def get_list(limit: Annotated[int, Query(ge=1, le=1000)] = 10, offset: Annotated[int, Query(ge=0)] = 0) -> List[RecordResponse]:
    print(f'Paginado limite {limit} y offset {offset}')
    return controller.get_list(limit, offset)


@router.get(
    '/{expedienteId}',
    status_code=200,
    responses={
        200: {'description': 'Expediente encontrado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es un entero válido'},
    },
    description='Retorna un expediente por ID. Falla si el ID no existe.'
    )  # GET /expedientes/{ID}
async def get_by_ID(id: Annotated[int, Path(ge=1)]) -> RecordResponse:
    return controller.get_by_id(id)

@router.patch(
    '/{expedienteId}',
    status_code=200,
    responses={
        200: {'description': 'Expediente encontrado'},
        404: NotFound.as_dict(),
        422:{'description': 'ID no es un entero válido'},
    },
    description='Actualiza un expediente con la data de Body Param. Falla si el ID no existe.'
    )  # PATCH /expedientes/{ID}
async def update(id: Annotated[int, Path(ge=1)], record: RecordRequest) -> RecordResponse:
    return controller.update(id, record)

@router.delete(
    '/{expedienteId}',
    status_code=200,
    responses={
        200: {'description': 'Expediente eliminado'},
        404: NotFound.as_dict(),
        422:{'description': 'ID no es un entero válido'},
    },
    description='Elimina un expediente con ID pasado por path Param. Falla si el ID no existe.'
    )  # DELETE /expedientes/{ID}
async def delete(id: Annotated[int, Path(ge=1)]) -> None:
    return controller.delete(id)