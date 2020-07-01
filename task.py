import datetime

class Ticket:

    tickets_pool = []

    def __init__(self, task=None):
        self._task = task
        self._open_date = None
        self._closure_date = None
        self._status = None
        self._assigned_user = None

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
    def assigned_user(self):
        return self._assigned_user

    @assigned_user.setter
    def assigned_user(self, user):
        self._assigned_user = user

    def create_ticket(self, task, closure_date, user):
        self.task = task
        self.open_date = datetime.date.today()
        self.closure_date = closure_date
        self.assigned_user = user
        self.status = 'Open'

    def is_expired(self):
        return self._closure_date < datetime.date.now()

    def __repr__(self):
        return "Ticket({}, {}, {}, {})".format(self._open_date,
                                                   self._closure_date,
                                                   self._task,
                                                   self._status)
