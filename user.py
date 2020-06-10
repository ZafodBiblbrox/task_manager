class User:

    def __init__(self, position, name, email, login, password, access_level):
        self.position = position
        self.name = name
        self.email = email
        self.login = login
        self.password = password
        self.access_level = access_level

    def perform_login(self, login, password):
        pass

    def create_ticket(self):
        pass

    def receive_ticket(self, ticket):
        pass

    def reassign_ticket(self, user):
        pass

    def extend_ticket_date(self, ticket):
        pass

    def determine_closure_date(self, ticket):
        pass

    def confirm_closure(self, ticket):
        pass

