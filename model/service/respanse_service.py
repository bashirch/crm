from controller.exceptions.exeptions import ResponseReportNotFoundError
from model.da.da import DataAccess
from model.entity import response
from model.entity.response import Response


class ResponseService:
    @staticmethod
    def save(response):
        response_da = DataAccess(Response)
        response_da.save(response)

    @staticmethod
    def edit(response):
        response_da = DataAccess(Response)
        if response_da.find_by_id(response.id):
            response_da.edit(response)
            return response
        else:
            raise ResponseReportNotFoundError

    @staticmethod
    def remove(id):
        response_da = DataAccess(Response)
        if response_da.find_by_id(id):
            return response_da.remove(id)
        else:
            raise ResponseReportNotFoundError

    @staticmethod
    def find_all():
        response_da = DataAccess(Response)
        return response_da.find_all()

    @staticmethod
    def find_by_id(id):
        response_da = DataAccess(Response)
        return response_da.find_by_id(id)

    @staticmethod
    def find_by_date_time(date_time):
        response_da = DataAccess(Response)
        return response_da.find_by_date_time(date_time)

    @staticmethod
    def find_by_serial(serial):
        response_da = DataAccess(Response)
        return response_da.find_by_serial(serial)
