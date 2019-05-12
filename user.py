class User:
    def __init__(self, login, password, nom, prenom):
        self.login = login
        self.password = password
        self.nom = nom
        self.prenom = prenom

    def get_login(self):
        return self.login
    def get_password(self):
        return self.password
    def get_nom(self):
        return self.nom
    def get_prenom(self):
        return self.prenom
    def set_login(self,login):
        self.login = login