import datetime

from model.entity import Response
from model.service.respanse_service import ResponseService


response = Response("bashir","asdasd", True)
ResponseService.save(response)
print(response)