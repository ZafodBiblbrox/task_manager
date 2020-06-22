from task import Ticket
import datetime

class User:

    users = []

    def __init__(self):
        self._login = None
        self._password = None
        self._name = None
        self._created_tickets = {}
        self._assigned_tickets = {}
        self._authorized = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        self._login = login

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def is_authorized(self, name, login, password):
        self._name = name
        self._login = login
        self._password = password
        if all([self._name, self._login, self._password]):
            return True

        return False

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


