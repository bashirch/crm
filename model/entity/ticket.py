from sqlalchemy import Column, Integer, String, Boolean, DateTime
from model.entity.base import Base
from model.tools.validator import *


class Ticket(Base):
    __tablename__ = "ticket_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String, nullable=False)
    _description = Column("description", String, nullable=False)
    _date = Column("date", DateTime, nullable=False)
    _status = Column("status", String, nullable=False)
    _deleted = Column("deleted", Boolean, nullable=False, default=False)

    def __init__(self, name, description, date, status, deleted):
        self.id = None
        self.name = name
        self.description = description
        self.date = date
        self.status = status
        self.deleted = deleted
