from model.service.client_service import *

client = Client("bashir", "charkhab", "ahvaz", "065073477", "2024-07-07")
ClientService.save(client)
print(client)
print(ClientService.find_by_id(7))
# ClientService.remove(7)
print(ClientService.find_all())
