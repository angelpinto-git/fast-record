

class ExpedientesRepository:
    last_id: int = 0
    fake_db: list[dict] = []

    def create(self, new_record: dict) -> dict:
        from datetime import datetime # No se recomienda hacer este from, es a modo de ejemplo para este caso, va hacer un import dentro de una función
        now = datetime.now()
        ExpedientesRepository.last_id += 1
        new_record.update(
            id=ExpedientesRepository.last_id,
            created_at=now,
            updated_at=now,
        )
        ExpedientesRepository.fake_db.append(new_record)
        return new_record
    
    def get_list(self, limit: int, offset: int) -> list[dict]:
        db_size = len(ExpedientesRepository.fake_db)
        first_index = min(db_size, offset)
        last_index = min(db_size, (first_index + limit))
        return ExpedientesRepository.fake_db[first_index:last_index]
    
    def get_id(self, id: int) -> dict | None:
        for record in ExpedientesRepository.fake_db:
            if record['id'] == id:
                return record

    def update(self, id: int, new_data: dict) -> dict:
        from datetime import datetime # En este caso se pone el import en la función, siempre se pone al comienzo del archivo
        now = datetime.now()
        current_record = self.by_id(id)
        if current_record is None: return 
        current_record.update(**new_data, updata_at=now)
        return current_record
    
    def delete(self, id: int) -> bool:
        current_record = self.__fake_by_id(id)
        if current_record is None: return False
        ExpedientesRepository.fake_db.remove(current_record)
        return True  