class ClientReportNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Client Not Found !!!")
