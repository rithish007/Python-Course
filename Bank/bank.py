class Bank:
    def __init__(self, uname, upass):
        self.username = uname
        self.password = upass

    def print_details(self):
        print(f'Username: {self.username}, Password: {self.password}')


class Login(Bank):
    def __init__(self, uname, upass):
        Bank.__init__(self, uname, upass)

    def id(self):
        print(f'{self.username} is logged in succesfully')


if __name__ == "__main__":
    s = Login('Bank, bank@123')
    s.print_details()
    s.id()
