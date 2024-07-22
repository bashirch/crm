from sqlalchemy import Column, Integer, String, Boolean, DateTime
from model.entity import *
from model.tools.validator import *


class Client(Base):
    __tablename__ = "client_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(30))
    _family = Column("family", String(30))
    _city = Column("city", String(30))
    _phone = Column("phone", String(30))
    _status = Column("status", Boolean, default=True)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, name, family, city, phone):
        self._id = None
        self._name = name
        self._family = family
        self._city = city
        self._phone = phone
        self._status = True
        self._deleted = False

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
    @pattern_validator(r"^[A-Za-z]{3-30}$", "Invalid Client Name")
    def name(self, name):
        self._name = name

    @property
    def family(self):
        return self._family

    @family.setter
    @pattern_validator(r"^[A-Za-z]{3-30}$", "Invalid Client Family")
    def family(self, family):
        self._family = family

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def phone(self):
        return self._phone
    #todo
    @phone.setter
    @pattern_validator(r"^/d{9}$", "Invalid Phone Number")
    def phone(self, phone):
        self._phone = phone

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
