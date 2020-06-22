import datetime

class Ticket:

    tickets_pool = []

    def __init__(self, task=None):
        self._task = task
        self._open_date = None
        self._closure_date = None
        self._status = None
        self._ticket_no = None

    @property
    def open_date(self):
        return self._open_date

    @open_date.setter
    def open_date(self, open_date):
        self._open_date = open_date

    @property
    def closure_date(self):
        return self._closure_date

    @closure_date.setter
    def closure_date(self, close_date):
        self._closure_date = close_date

    @property
    def status(self):
        print(self._status)
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, task):
        self._task = task

    @property
    def ticket_no(self):
        return self._ticket_no

    @ticket_no.setter
    def ticket_no(self, ticket_no):
        self._ticket_no = ticket_no

    def create_ticket(self, task, closure_date):
        self.task = task
        self.open_date = datetime.date.today()
        self.closure_date = closure_date
        self.ticket_no = id

    def is_expired(self):
        return self._closure_date < datetime.date.now()

    def __repr__(self):
        return "Ticket({}, {}, {}, {}, {})".format(self._open_date,
                                                   self._closure_date,
                                                   self._task,
                                                   self._status,
                                                   self._ticket_no)
