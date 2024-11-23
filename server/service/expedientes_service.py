from typing import List

from server.schemas.expedientes_schemas import NewRecordRequest, RecordResponse, RecordRequest
from server.exceptions import NotFound

class ExpedientesService:
    last_id: int = 0
    fake_db: list[dict] = []

    def __init__(self):
        # TODO: instanciar repo
        pass

    def create(self, new_record: NewRecordRequest) -> RecordResponse:
        # TODO
        #! 1. Recibir el objeto de tipo NewRecordResponse, convertirlo a diciconario, y pasarlo a la capa de repositorio
        #! 2. Recibir del repo la respuesta(probablemente un diccionario o un objeto) convertirlo a RecordResponse y retornarlo
        #? Código de ejemplo
        record_dict = self.__fake_create(new_record.model_dump())
        return ExpedientesService(**record_dict)
                                  
    def get_list(self, limit: int, offset: int) -> List[RecordResponse]:
        # TODO:
        #! 1. Recibir los pará,etrps limit y offset y pasarlos a la capa repo
        #! 2. Recibir la lista de diccionarios u objetos, convertirlos a una lista de RecordResponse y retornarlo
        #? Código de ejemplo
        record_list = self.__fake_get_list(limit, offset)
        return [RecordResponse(**record) for record in record_list]

    def get_by_id(self, id:int) -> RecordResponse:
        # TODO:
        #! 1. Recibir el id de los parámetros y pasarlo a la capa de repo
        #! 2. Recibir el objeto o dicionario del repo, lo convertimos a un RecordResponse y retronarlo
        #? Código de ejemplo
        record = self.__fake_get_by_id(id)
        if record is None:
            raise NotFound(f'Proyecto con id #{id} no encontrado')
        return RecordResponse(**record)      
        
    def update(self, id: int, new_data: RecordRequest) -> RecordResponse:
        # TODO:
        #! 1. Recibir los parámetros, convertir en new_data a un dicionario y lo pasamos al repo
        #! 2. Recibimos el objeto o diccionario acutalizado del repo, lo convertimos a RecordResponse y lo retornamos
        #? Código de ejemplo
        updated_record = self.__fake_update(id, new_data.model_dump(exclude_none=True))
        if updated_record is None:
            raise NotFound(f'Proyecto con id #{id} no encontrado para actualizarse')
        return RecordResponse(**updated_record)

    def delete(self, id: int) -> None:
        # TODO:
        #! 1. Pasamos el id al repo y retornamos
        #? Código de ejemplo
        if not self.__salfe_delete(id):
            raise NotFound(f'Proyecto con id #{id} no encontrado para eliminarse')

    #? FAKE METHODS (Son los que van a Simular la interección con la capa de repositorio)
    def __fake_create(self, new_record: dict) -> dict:
        from datetime import datetime # No se recomienda hacer este from, es a modo de ejemplo para este caso, va hacer un import dentro de una función
        now = datetime.now()
        ExpedientesService.last_id += 1
        new_record.update(
            id=ExpedientesService.last_id,
            created_at=now,
            updated_at=now,
        )
        ExpedientesService.fake_db.append(new_record)
        return new_record
    
    def __fake_get_list(self, limit: int, offset: int) -> list[dict]:
        db_size = len(ExpedientesService.fake_db)
        first_index = min(db_size, offset)
        last_index = min((db_size - first_index), limit)
        return ExpedientesService.fake_db[first_index:last_index]
    
    def __fake_get_id(self, id: int) -> dict | None:
        for record in ExpedientesService.fake_db:
            if record['id'] == id:
                return record

    def __fake_update(self, id: int, new_data: dict) -> dict:
        from datetime import datetime # En este caso se pone el import en la función, siempre se pone al comienzo del archivo
        now = datetime.now()
        current_record = self.__fake_by_id(id)
        if current_record is None: return 
        current_record.update(**new_data, updata_at=now)
        return current_record
    
    def __fake_delete(self, id: int) -> bool:
        current_record = self.__fake_by_id(id)
        if current_record is None: return False
        ExpedientesService.fake_db.remove(current_record)
        return True