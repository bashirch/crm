class ClientReportNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Client Not Found !!!")

class TicketReportNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Ticket Not Found !!!")

class RespanseReportNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Respanse Not Found !!!")

