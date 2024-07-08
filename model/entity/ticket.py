from sqlalchemy import Column, Integer, String, Boolean, DateTime
from model.entity import *
from model.tools.validator import *


class Ticket(Base):
    __tablename__ = "ticket_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(30), nullable=False)
    _description = Column("description", String(30), nullable=False)
    _ticket_date_time = Column("ticket_date_time", DateTime, nullable=False)
    _status = Column("status", String(30), nullable=False)
    _deleted = Column("deleted", Boolean, nullable=False, default=False)

    def __init__(self, name, description, status, deleted=False):
        self.id = None
        self.name = name
        self.description = description
        self._ticket_date_time = None
        self.status = status
        self.deleted = deleted
