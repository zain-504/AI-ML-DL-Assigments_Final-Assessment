class login:
    def __init__(self):
        self.username = "Admin"
        self.password = "123"

    def authenticate(self):
            user = input("Enter User Name: ")
            pwd = input("Enter Password: ")

            if user == self.username and pwd == self.password:
                print("Login Successfully!")
                

            else:
                print("Invalid user name or password!")


login = login()
login.authenticate()