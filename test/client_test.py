from datetime import datetime

from model.entity import Client
from model.service.client_service import ClientService

client = Client("ba#shir", "char@khab", "ahv@az", "+98a936507a3477")
ClientService.save(client)
print(client)
# print(ClientService.find_by_id(7))
# ClientService.remove(7)
# print(ClientService.find_all())
