from app.db import DB, Schema
from sqlalchemy import Column, Integer, String, DateTime


class Candidate(DB.Base):
    __tablename__ = Schema.Tables.Candidate
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    up_date = Column(DateTime, nullable=False)
    down_date = Column(DateTime, nullable=True)

    @staticmethod
    def find_all():
        return DB.get_session().query(Candidate).all()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.first_name,
            "last_name": self.last_name,
            "full_name": "{} {}".format(self.first_name, self.last_name),
            "up_date": str(self.up_date)
        }
