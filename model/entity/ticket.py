from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

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
        self._id = None
        self._name = name
        self._description = description
        self._ticket_date_time = None
        self._status = status
        self._deleted = deleted

    owner_id = Column(Integer, ForeignKey("client_tbl.id") )
    owner = relationship("Client")

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    @pattern_validator(r"^[A-Za-z0-9]+$", "Invalid Client Name")
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def ticket_date_time(self):
        return self._ticket_date_time

    @ticket_date_time.setter
    @date_time_validator("Invalid Date Time!!!")
    def ticket_date_time(self, ticket_date_time):
        self._ticket_date_time = ticket_date_time

    @property
    def status(self):
        return self._status

    @status.setter
    @boolean_validator("Invalid Status")
    def status(self, status):
        self._status = status

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    @boolean_validator("Invalid Status")
    def deleted(self, deleted):
        self._deleted = deleted
