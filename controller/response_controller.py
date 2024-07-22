from model.service.respanse_service import ResponseService
from model.tools.logger import Logger


class ResponseController:
    @staticmethod
    def save(response):
        try:
            ResponseService.save(response)
            Logger.info(f"Response Saved - {response}")
            return True, response
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit(response):
        try:
            if ResponseService.find_by_id(response.id):
                ResponseService.edit(response)
                Logger.info(f"Response Edited - {response}")
                return response
            else:
                pass
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove(id):
        try:
            response = ResponseService.remove(id)
            Logger.info(f"response Removed - {response}")
            return True, response

        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_all():
        try:
            response_list = ResponseService.find_all()
            Logger.info(f"Response Find All()")
            return True, response_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_id(id):
        try:
            response = ResponseService.find_by_id(id)
            Logger.info(f"Response Find By Id({id})")
            return True, response
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_date_time(date_time):
        try:
            return ResponseService.find_by_date_time(date_time)
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"
