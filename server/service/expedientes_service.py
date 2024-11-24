from typing import List

from server.schemas.expedientes_schemas import NewRecordRequest, RecordResponse, RecordRequest
from server.exceptions import NotFound
from server.repository import ExpedientesRepository

class ExpedientesService:
    
    def __init__(self):
        self.record_repo = ExpedientesRepository()

    def create(self, new_record: NewRecordRequest) -> RecordResponse:
        record_dict = self.record_repo.create(new_record.model_dump())
        return RecordResponse(**record_dict)
                                  
    def get_list(self, limit: int, offset: int) -> List[RecordResponse]:
        record_list = self.record_repo.get_list(limit, offset)
        return [RecordResponse(**record) for record in record_list]

    def get_by_id(self, id:int) -> RecordResponse:
        record = self.record_repo.get_by_id(id)
        if record is None:
            raise NotFound(f'Proyecto con id #{id} no encontrado')
        return RecordResponse(**record)      
        
    def update(self, id: int, new_data: RecordRequest) -> RecordResponse:
        updated_record = self.record_repo.update(id, new_data.model_dump(exclude_none=True))
        if updated_record is None:
            raise NotFound(f'Proyecto con id #{id} no encontrado para actualizarse')
        return RecordResponse(**updated_record)

    def delete(self, id: int) -> None:
        if not self.record_repo.delete(id):
            raise NotFound(f'Proyecto con id #{id} no encontrado para eliminarse')
           