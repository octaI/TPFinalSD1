from datetime import datetime

from sqlalchemy.orm import relationship

from app.db import DB, Schema
from sqlalchemy import Column, Integer, DateTime


class Vote(DB.Base):
    __tablename__ = Schema.Tables.Vote
    id = Column(Integer, primary_key=True)
    reference = Column(Integer, nullable=False)
    up_date = Column(DateTime, nullable=False)


    @classmethod
    def get_all(cls):
        return DB.get_session().query(cls).all()

    @classmethod
    def get_candidate_votes(cls, candidate_id):
        print(candidate_id)
        return DB.get_session().query(cls).filter(Vote.reference == candidate_id).all()

    def to_dict(self):
        return {
            "id": str(self.id),
            "Reference": str(self.reference),
            "up_date": self.up_date
        }

    @classmethod
    def insert_vote(cls, candidate_id):
        session = DB.get_session()
        new_vote = Vote(
                reference=candidate_id,
                up_date=datetime.now()
        )
        session.add(new_vote)
        session.flush()
        session.refresh(new_vote)
        id_to_return = new_vote.id
        session.commit()
        return id_to_return

