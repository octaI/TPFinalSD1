from datetime import datetime

from app.db import DB, Schema
from sqlalchemy import Column, Integer, String, DateTime


class Candidate(DB.Base):
    __tablename__ = Schema.Tables.Candidate
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    up_date = Column(DateTime, nullable=False)
    down_date = Column(DateTime, nullable=True)

    @classmethod
    def find_all(cls):
        return DB.get_session().query(cls).all()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.first_name,
            "last_name": self.last_name,
            "full_name": "{} {}".format(self.first_name, self.last_name),
            "up_date": str(self.up_date)
        }

    @classmethod
    def create(cls, data):
        session = DB.get_session()
        session.add_all([
            Candidate(
                first_name=data["first_name"],
                last_name=data["last_name"],
                up_date=datetime.now()
            )
        ])
        session.commit()
