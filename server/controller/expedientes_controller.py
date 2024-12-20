import logging
from typing import List

from server.schemas.expedientes_schemas import NewRecordRequest, RecordResponse, RecordRequest
from server.exceptions import BaseHTTPException, InternalServerError
from server.service import ExpedientesService


logger = logging.getLogger(__name__)


class ExpedientesController:
    def __init__(self):
        self.service = ExpedientesService()

    
    def create(self, new_record: NewRecordRequest) -> RecordResponse:
        try:
            logger.debug(f'Crear expediente {new_record.cover}')
            return self.service.create(new_record)
        except BaseHTTPException as ex:
            logger.error('Error al procesar request, status code {ex.status_code}: {ex.description}')
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(f'Error no contemplado en {__name__}.create')
            raise InternalServerError(str(ex))

    def get_list(self, limit: int, offset: int) -> List[RecordResponse]:
        try:
            return self.service.get_list(limit, offset)
        except BaseHTTPException as ex:
            logger.error('Error al procesar request, status code {ex.status_code}: {ex.description}')
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(f'Error no contemplado en {__name__}.get_list')
            raise InternalServerError(str(ex))

 

    def get_by_id(self, record_id: int) -> RecordResponse:
        try:
            logger.debug(f'Buscar expediente #{record_id}')
            return self.service.get_by_id(id)
        except BaseHTTPException as ex:
            logger.error('Error al procesar request, status code {ex.status_code}: {ex.description}')
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(f'Error no contemplado en {__name__}.get_by_id')
            raise InternalServerError(str(ex))

        

    def update(self, record_id: int, new_data: RecordRequest) -> RecordResponse:
        try:
            return self.service.update(record_id, new_data)
        except BaseHTTPException as ex:
            logger.error('Error al procesar request, status code {ex.status_code}: {ex.description}')
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(f'Error no contemplado en {__name__}.update')
            raise InternalServerError(str(ex))

        

    def delete(self, record_id: int) -> None:
        try:
            self.delete(id)
        except BaseHTTPException as ex:
            logger.error('Error al procesar request, status code {ex.status_code}: {ex.description}')
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(f'Error no contemplado en {__name__}.delete')
            raise InternalServerError(str(ex))

    def __handler_http_exception(self, ex: BaseHTTPException):
        if ex.status_code >= 500:
            logger.critical(f'Error en el servidor con status code {ex.status_code}: {ex.description}')
        else:
            logger.error(f'Error {ex.status_code}: {ex.description}')
        raise ex

