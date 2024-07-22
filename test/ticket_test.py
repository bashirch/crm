from model.entity import Ticket
from model.service.ticket_service import TicketService

ticket = Ticket("bashir" , "dsjnasdasda ndlkas" , True)
TicketService.save(ticket)
print(ticket)