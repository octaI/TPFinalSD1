from app.db import DB, Schema
from sqlalchemy import Column, Integer, VARCHAR, DATETIME


class Vote(DB.Base):
    __tablename__ = Schema.Tables.Vote
    id = Column(Integer, primary_key=True)
    reference = Column(Integer, nullable=False, unique=True)
    up_date = Column(DATETIME, nullable=False)