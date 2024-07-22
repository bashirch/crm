from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model.entity import *
from model.tools.validator import *


class Response(Base):
    __tablename__ = "response_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(30))
    _description = Column("description", String(100))
    _response_date_time = Column("response_date_time", DateTime)
    _status = Column("status", Boolean, default=False)
    _deleted = Column("deleted", Boolean, default=False)

    _owner_id = Column(Integer, ForeignKey("ticket_tbl.id") )
    owner = relationship("Ticket")

    def __init__(self, name, description, status, deleted=False):
        self._id = None
        self._name = name
        self._description = description
        self._response_date_time = None
        self._status = status
        self._deleted = deleted


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
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def response_date_time(self):
        return self._response_date_time

    @response_date_time.setter
    @date_time_validator
    def Response_date_time(self, response_date_time):
        self._response_date_time = response_date_time

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