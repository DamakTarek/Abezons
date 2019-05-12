from user import User
class Client(User):
    def __init__(self, login, password, nom, prenom, cb):
        super(Client, self).__init__(login, password, nom, prenom)
        self.cb = cb

    def get_cb(self):
        return self.cb