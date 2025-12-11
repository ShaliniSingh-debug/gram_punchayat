from sqlalchemy import create_engine , engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./gram_punchayat_complaints.db'

connect_args =  {"check_same_thread": False}
engine = create_engine(SQLALCHEMY_DATABASE_URL , connect_args= connect_args)

sessionLocal = sessionmaker(bind=engine , autocommit = False  , autoflush= False)
Base = declarative_base()

def get_db():
              db = sessionLocal()
              try:
                            yield db
              finally:
                            db.close() 
                            