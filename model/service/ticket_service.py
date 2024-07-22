from datetime import datetime

from controller.exceptions.exeptions import TicketReportNotFoundError
from model.da.da import DataAccess
from model.entity import ticket


class TicketService:
    @staticmethod
    def save(ticket):
        ticket_da = DataAccess(ticket)
        ticket._ticket_date_time = datetime.now()
        ticket_da.save(ticket)

    @staticmethod
    def edit(ticket):
        ticket_da = DataAccess(ticket)
        if ticket_da.find_by_id(ticket.id):
            ticket_da.edit(ticket)
            return ticket
        else:
            raise ticketReportNotFoundError

    @staticmethod
    def remove(id):
        ticket_da = DataAccess(ticket)
        if ticket_da.find_by_id(id):
            return ticket_da.remove(id)
        else:
            raise ticketReportNotFoundError()

    @staticmethod
    def find_all():
        ticket_da = DataAccess(ticket)
        return ticket_da.find_all()

    @staticmethod
    def find_by_id(id):
        ticket_da = DataAccess(ticket)
        return ticket_da.find_by_id(id)

    @staticmethod
    def find_by_date_time(date_time):
        ticket_da = DataAccess(ticket)
        return ticket_da.find_by_date_time(date_time)

    @staticmethod
    def find_by_serial(serial):
        ticket_da = DataAccess(ticket)
        return ticket_da.find_by_serial(serial)
