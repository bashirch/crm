from model.service.respanse_service import RespanseService
from model.tools.logger import Logger


class RespanseController:
    @staticmethod
    def save(respanse):
        try:
            RespanseService.save(respanse)
            Logger.info(f"Respanse Saved - {respanse}")
            return True, respanse
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def edit(respanse):
        try:
            if RespanseService.find_by_id(respanse.id):
                RespanseService.edit(respanse)
                Logger.info(f"Respanse Edited - {respanse}")
                return respanse
            else:
                pass
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def remove(id):
        try:
            respanse = RespanseService.remove(id)
            Logger.info(f"Respanse Removed - {respanse}")
            return True, respanse

        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_all():
        try:
            respanse_list = RespanseService.find_all()
            Logger.info(f"Respanse Find All()")
            return True, respanse_list
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_id(id):
        try:
            respanse = RespanseService.find_by_id(id)
            Logger.info(f"Respanse Find By Id({id})")
            return True, respanse
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"

    @staticmethod
    def find_by_date_time(date_time):
        try:
            return RespanseService.find_by_date_time(date_time)
        except Exception as e:
            Logger.error(f"{e}")
            return False, f"{e}"
