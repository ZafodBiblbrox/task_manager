from task import Ticket
import datetime

class User:

    def __init__(self, name=None):
        self._login = None
        self._password = None
        self._name = name
        self._assigned_tickets = []

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
        task_obj = Ticket(task)
        task_obj.open_date = datetime.date.today()
        self._assigned_tickets.append(task_obj)
        task = task_obj.task
        ticket_id = self._assigned_tickets.index(task)
        task_obj.ticket_no = ticket_id

    def define_closure_date(self, task_obj, year, month, day):
        task_obj.closure_date = datetime.date(year, month, day)

    def get_user_tickets(self):
        user_tasks =  self._assigned_tickets
        return user_tasks

    def receive_ticket(self, ticket):
        pass

    def reassign_ticket(self, user):
        pass

    def extend_ticket_date(self, ticket):
        pass



    def confirm_closure(self, ticket):
        pass


