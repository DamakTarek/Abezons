from user import User
class Admin(User):
    def __init__(self, login, password, nom, prenom, grade):
        super(Admin, self).__init__(login, password, nom, prenom)
        self.grade = grade

    def get_grade(self):
        return self.grade