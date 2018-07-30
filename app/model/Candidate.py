from datetime import datetime

from sqlalchemy.orm import aliased, relationship
from app.db import DB, Schema
from sqlalchemy import Column, Integer, String, DateTime, inspect


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
            "id": str(self.id),
            "name": self.first_name,
            "last_name": self.last_name,
            "full_name": "{} {}".format(self.first_name, self.last_name),
            "up_date": str(self.up_date)
        }

    @classmethod
    def find_candidate(cls, candidate_name):
        first_name = candidate_name.split(" ")[0]
        last_name = candidate_name.split(" ")[1]
        return DB.get_session().query(cls).filter(Candidate.first_name == first_name, Candidate.last_name == last_name)\
            .all()


    @classmethod
    def create(cls, data):
        if (len(cls.find_candidate(data["first_name"] + " " + data["last_name"])) > 0):
            return
        session = DB.get_session()
        session.add_all([
            Candidate(
                first_name=data["first_name"],
                last_name=data["last_name"],
                up_date=datetime.now()
            )
        ])
        session.commit()