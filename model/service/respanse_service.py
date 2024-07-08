from controller.exceptions.exeptions import RespanseReportNotFoundError
from model.da.da import DataAccess
from model.entity import response
from model.entity.response import Response


class RespanseService:
    @staticmethod
    def save(respanse):
        respanse_da = DataAccess(Response)
        respanse_da.save(respanse)

    @staticmethod
    def edit(respanse):
        respanse_da = DataAccess(Response)
        if respanse_da.find_by_id(respanse.id):
            respanse_da.edit(respanse)
            return respanse
        else:
            raise RespanseReportNotFoundError

    @staticmethod
    def remove(id):
        respanse_da = DataAccess(Response)
        if respanse_da.find_by_id(id):
            return respanse_da.remove(id)
        else:
            raise RespanseReportNotFoundError()

    @staticmethod
    def find_all():
        respanse_da = DataAccess(Response)
        return respanse_da.find_all()

    @staticmethod
    def find_by_id(id):
        respanse_da = DataAccess(Response)
        return respanse_da.find_by_id(id)

    @staticmethod
    def find_by_date_time(date_time):
        respanse_da = DataAccess(Response)
        return respanse_da.find_by_date_time(date_time)

    @staticmethod
    def find_by_serial(serial):
        respanse_da = DataAccess(Response)
        return respanse_da.find_by_serial(serial)
