class User:

    users = []

    def __init__(self):
        self.user_login = None
        self.user_password = None
        self.user_name = None


    @property
    def name(self):
        return self.user_name

    @name.setter
    def name(self, name):
        self.user_name = name

    @property
    def login(self):
        return self.user_login

    @login.setter
    def login(self, login):
        self.user_login = login

    @property
    def password(self):
        return self.user_password

    @password.setter
    def password(self, password):
        self.user_password = password

    def is_validated(self, name, login, password):
        self.user_name = name
        self.user_login = login
        self.user_password = password
        if all([self.user_name, self.user_login, self.user_password]):
            #self.create_user(self.user_db)
            return True

        return False
