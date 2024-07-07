from controller.exceptions.exeptions import ClientReportNotFoundError
from model.da.da import DataAccess
from model.entity.client import *


class ClientService:
    @staticmethod
    def save(client):
        client_da = DataAccess(Client)
        client_da.save(client)

    @staticmethod
    def edit(client):
        client_da = DataAccess(Client)
        if client_da.find_by_id(client.id):
            client_da.edit(client)
            return client
        else:
            raise ClientReportNotFoundError

    @staticmethod
    def remove(id):
        client_da = DataAccess(Client)
        if client_da.find_by_id(id):
            return client_da.remove(id)
        else:
            raise ClientReportNotFoundError()

    @staticmethod
    def find_all():
        client_da = DataAccess(Client)
        return client_da.find_all()

    @staticmethod
    def find_by_id(id):
        client_da = DataAccess(Client)
        return client_da.find_by_id(id)

    @staticmethod
    def find_by_date_time(date_time):
        client_da = DataAccess(Client)
        return client_da.find_by_date_time(date_time)

    @staticmethod
    def find_by_serial(serial):
        client_da = DataAccess(Client)
        return client_da.find_by_serial(serial)
