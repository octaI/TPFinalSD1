# Todo: Initializer data of DB objects
from typing import List

from app import config
from app.model.Candidate import Candidate
from app.db import DB
import logging

def init():
    DB.Base.metadata.create_all(DB.Engine)
    if config.INIT.CREATE_CANDIDATES:
        logging.info("Creating candidates")
        Candidate.create({
            "first_name": "Alan",
            "last_name": "Touring"
        })
        Candidate.create({
            "first_name": "Barbara",
            "last_name": "Liskov"
        })


