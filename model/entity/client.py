from sqlalchemy import Column, Integer, String, Boolean, DateTime
from model.entity import *
from model.tools.validator import *


class Client(Base):
    __tablename__ = "client_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(30))
    _family = Column("family", String(30))
    _city = Column("city", String(30))
    _phone = Column("phone", Integer)
    _status = Column("status", Boolean, default=True)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, client_name, client_family, client_city, client_phone):
        self._id = None
        self._name = client_name
        self._family = client_family
        self._client_city = client_city
        self._client_phone = client_phone
        self._status = True
        self._deleted = False

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def client_name(self):
        return self._client_name

    @client_name.setter
    @pattern_validator(r"^[A-Za-z0-9]+$" , "Invalid Client Name")
    def client_name(self, client_name):
        self._client_name = client_name

    @property
    def client_family(self):
        return self._client_family

    @client_family.setter
    @pattern_validator(r"^[A-Za-z0-9]+$" , "Invalid Client Family")
    def client_family(self, client_family):
        self._client_family = client_family

    @property
    def client_city(self):
        return self._client_city

    @client_city.setter
    def client_city(self, client_city):
        self._client_city = client_city

    @property
    def client_phone(self):
        return self._client_phone

    @client_phone.setter
    @pattern_validator(r"^(+98 | 09)/d{9}+$" , "Phone Number")
    def client_phone(self, client_phone):
        self._client_phone = client_phone

    @property
    def client_calling_time(self):
        return self._client_calling_time

    @client_calling_time.setter
    @date_time_validator
    def client_calling_time(self, client_calling_time):
        self._client_calling_time = client_calling_time

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
