from fastapi import APIRouter
from typing import List, Dict, Optional
from config import database

from .models import students
from .schemas import Student


from sqlalchemy.orm import Session

post_route = APIRouter()


@post_route.get("/", response_model=List[Student], status_code=200)
async def get_all_students():
    query = students.select()
    get_all_students = await database.fetch_all(query)
    if students is None:
        return {"message": " No such student!"}
    else:
        return get_all_students



@post_route.get("/{id}", response_model=Student, status_code=200)
async def get_student(id:int):
    query = students.select().where(students.c.id == id)
    return await database.fetch_one(query=query)


@post_route.post("/create", response_model=Student, status_code=201)
async def create(student: Student):

    query = students.insert().values( name=student.name, surname=student.surname, email=student.email)
    last_record_id = await database.execute(query=query)
    return {**student.dict(), "id": last_record_id}


@post_route.put("/update/{id}", response_model=Student)
async def update(id:int, student: Student):
    query = students.update().where(students.c.id == id).values(
        name=student.name,
        surname=student.surname,
        email=student.email
        )
    last_record_id = await database.execute(query=query)
    return {**student.dict(), "id": last_record_id}


@post_route.delete("/delete/{id}", response_model=Student)
async def delete(id:int):
    query = students.delete().where(students.c.id == id)
    return await database.execute(query)