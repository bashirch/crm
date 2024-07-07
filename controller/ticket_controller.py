from model.service.ticket_service import TicketService
from model.tools.logger import Logger


class TicketController:
    @staticmethod
    def save(ticket):
        try:
            TicketService.save(ticket)
            Logger.info(f"Ticket Saved - {ticket}")
            return True, ticket
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit(ticket):
        try:
            if TicketService.find_by_id(ticket.id):
                TicketService.edit(ticket)
                Logger.info(f"Ticket Edited - {ticket}")
                return ticket
            else:
                pass
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove(id):
        try:
            ticket = TicketService.remove(id)
            Logger.info(f"Ticket Removed - {ticket}")
            return True, ticket

        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_all():
        try:
            ticket_list = TicketService.find_all()
            Logger.info(f"Ticket Find All()")
            return True, ticket_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_id(id):
        try:
            ticket = TicketService.find_by_id(id)
            Logger.info(f"Ticket Find By Id({id})")
            return True, ticket
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_date_time(date_time):
        try:
            return TicketService.find_by_date_time(date_time)
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"
