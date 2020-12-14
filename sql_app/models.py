import sqlalchemy
from config import metadata
from datetime import datetime


''' SQLAlchemy Model'''
students = sqlalchemy.Table(
    "students",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(200)),
    sqlalchemy.Column("surname", sqlalchemy.String(200)),
    sqlalchemy.Column("email", sqlalchemy.String(200), unique=True)

)