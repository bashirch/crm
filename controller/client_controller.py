from model.service.client_service import ClientService
from model.tools.logger import Logger


class ClientController:
    @staticmethod
    def save(client):
        try:
            ClientService.save(client)
            Logger.info(f"Client Saved - {client}")
            return True, client
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit(client):
        try:
            if ClientService.find_by_id(client.id):
                ClientService.edit(client)
                Logger.info(f"Client Edited - {client}")
                return client
            else:
                pass
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove(id):
        try:
            client = ClientService.remove(id)
            Logger.info(f"Client Removed - {client}")
            return True, client

        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_all():
        try:
            client_list = ClientService.find_all()
            Logger.info(f"Client Find All()")
            return True, client_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_id(id):
        try:
            client = ClientService.find_by_id(id)
            Logger.info(f"Client Find By Id({id})")
            return True, client
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_date_time(date_time):
        try:
            return ClientService.find_by_date_time(date_time)
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"
