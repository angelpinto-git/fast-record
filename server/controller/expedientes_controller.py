import logging
from typing import List

logger = logging.getLogger(__name__)

from server.schemas.expedientes_schemas import NewRecordRequest, RecordResponse, RecordRequest
from server.exceptions import BaseHTTPException, InternalServerError
from server.service import ExpedientesService


class ExpedientesController:
    def __init__(self):
        self.service = ExpedientesService()

    
    def create(self, new_record: NewRecordRequest) -> RecordResponse:
        try:
            logger.debug(f'Crear expediente {new_record.cover}')
            return self.service.create(new_record)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.create')
            raise InternalServerError()

    def get_list(self, limit: int, offset: int) -> List[RecordResponse]:
        try:
            return self.service.get_list(limit, offset)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.get_list')
            raise InternalServerError()

 

    def get_by_id(self, record_id: int) -> RecordResponse:
        try:
            logger.debug(f'Buscar expediente #{record_id}')
            return self.service.get_by_id(id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.get_by_id')
            raise InternalServerError()

        

    def update(self, id: int, new_data: RecordRequest) -> RecordResponse:
        try:
            return self.service.update(id, new_data)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.update')
            raise InternalServerError()

        

    def delete(self, id: int) -> None:
        try:
            self.delete(id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en {__name__}.delete')
            raise InternalServerError()

    def __handler_http_exception(self, ex: BaseHTTPException):
        if ex.status_code >= 500:
            logger.critical(f'Error en el servidor con status code {ex.status_code}: {ex.description}')
        else:
            logger.error(f'Error {ex.status_code}: {ex.description}')
        raise ex

