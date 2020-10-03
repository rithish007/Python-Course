class BankAccount:
    def __init__ (self, uname, upass, Balance = 10000):
        self.uname = uname
        self.upass = upass
        self.Balance = Balance

    def Transactions(self, ch):
        options = {1: "Deposit"
                   2: "Withdraw"
                   3: "Exit"}
        
    def id_details(self, uname, upass):
        print(f'Username: {self.uname}, Password: {self.upass}')

    def deposit(self, amount):
        self.deposit = self.Balance + self.amount
        print (f'\nThe current balance is = {self.deposit}')

    def withdraw(self, amount):
        self.withdraw = self.Balance - self.withdraw
        print(f'\nThe current balance is = {self.withdraw}')



if __name__ == "__main__":
    Username = input("Enter the Username :\t")
    Password = input("Enter the Password :\t")
    if Password != 'Bank@123':
        sys.exit()
    else:
        print(f"\nPress 1 to Deposit\nPress 2 to withdraw\nPress 3 to Transfer")
        restart = "yes"
    while restart[0] == "Y" or restart[0] == "y":
        ch = eval(input("Select an option :\t"))
        if (selection == 1):
            print(f'Enter the amount to DEPOSIT = ')
            restart = input('Do you want to continue. press (Yes/No)')
            
        elif (selection == 2):
            print(f'Enter the amount to WITHDRAW = ')
            restart = input('Do you want to continue. press (Yes/No)')
            
        else:
            print(f'Exiting...')
            sys.exit()

o = BankAccount(self)
o.deposit
o.withdraw