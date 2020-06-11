from task import Ticket
import datetime

class User:

    def __init__(self, name):
        self._login = None
        self._password = None
        self._name = name
        self._created_tickets = {}
        self._assigned_tickets = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def log_in_system(self, login, password):
        self._login = login
        self._password = password

    def create_ticket(self, task):
        ticket_obj = Ticket(task)
        ticket_obj.open_date = datetime.date.today()
        ticket_id = len(self._created_tickets) + 1
        self._created_tickets[ticket_id] = ticket_obj
        ticket_obj.ticket_no = ticket_id
        Ticket.tickets_pool[self.name] = {ticket_id: ticket_obj.task}

    def define_closure_date(self, ticket_obj, year, month, day):
        ticket_obj.closure_date = datetime.date(year, month, day)

    def assign_ticket(self, ticket_obj, user, year, month, day):
        ticket_id = ticket_obj.ticket_no
        ticket_from_user = self.name
        user._assigned_tickets[ticket_from_user] = {ticket_id: ticket_obj}
        self.define_closure_date(ticket_obj, year, month, day)

    def get_user_tickets(self):
        user_tickets = [ticket_obj for ticket_obj in self._created_tickets.values()]
        return user_tickets

    def get_user_assigned_tickets(self):
        for k, v in self._assigned_tickets.items():
            print(k, v)

    def receive_ticket(self, ticket):
        pass

    def extend_ticket_date(self, ticket):
        pass

    def confirm_closure(self, ticket):
        pass


