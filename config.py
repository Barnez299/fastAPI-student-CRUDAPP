from fastapi import FastAPI
import databases
import sqlalchemy

# import app


app = FastAPI()


''' DATABASE CONNECTION '''
DATABASE_URL = "postgresql://postgres:123456789@localhost/students"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# Base = declarative_base()