from sqlalchemy import Column, Integer, String, Boolean, DateTime
from model.entity.base import Base
from model.tools.validator import *


class Respanse(Base):
    __tablename__ = "respanse_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(30))
    _description = Column("description", String(100))
    _date = Column("date", DateTime)
    _status = Column("status", Boolean, default=False)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, name, description, date, status, deleted):
        self._id = id
        self._name = None
        self._description = description
        self._date = date
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
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

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