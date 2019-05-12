from client import Client

class LoginService:
    def __init__(self):
        self.users_list=[]
    def add_users(self, user):
        self.users_list.append(user)
    def get_users(self):
        return self.users_list
    def login(self, login, password):
        for user in self.users_list:
            if user.get_login()==login and user.get_password()==password:
                if isinstance(user,Client):
                    print ("connected as " + user.get_nom() + "  Client")
                    return 1
                else:
                    print ("connected as " + user.get_nom() + "  Admin")
                    return 2
        print("Login mnayek")
        return 0
