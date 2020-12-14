
from typing import List, Dict, Optional
from pydantic import BaseModel
from typing import Optional
from pydantic import validator
from pydantic.dataclasses import dataclass


''' Model Schema Using Pydantic '''


class Student(BaseModel):
    id: Optional[int]
    name: Optional [str]
    surname: Optional [str]
    email: Optional [str]

# code could be incorrect because id - changed to optional takes away error validation