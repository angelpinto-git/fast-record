from datetime import datetime

from pydantic import BaseModel


class NewRecordRequest(BaseModel) :
    cover: str
    status: str = 'new'
    description: str = ''

class RecordRequest(BaseModel) :
    cover : str | None = None
    status: str | None = None 
    description: str | None = None

class RecordResponse(BaseModel) :
    record_id: int
    cover: str
    status: str = 'new'
    description: str = ''
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    