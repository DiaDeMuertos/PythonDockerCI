from sqlalchemy import create_engine,  Column, Integer, Sequence, String, Date, Float, BIGINT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  fullname = Column(String)
  password = Column(String)

  def __repr__(self):
     return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

engine = create_engine('postgresql+psycopg2://postgres:123@db:5432/glen-db');
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = Session()