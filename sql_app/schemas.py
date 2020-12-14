
from pydantic import BaseModel


''' Model Schema Using Pydantic '''


class Student(BaseModel):
    id: int
    name: str
    surname: str
    email: str