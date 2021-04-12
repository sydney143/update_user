class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        print("okay")

    def make_withdrawal(self, amount):
        self.balance = self.balance - amount
        print(self.balance)
        return self
    
    def make_deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance} ")

an = User("Bob")
ok = User("Sydney")
get = User("Chris")

# First User:Bob
an.make_withdrawal(100)
an.make_deposit(200)
an.make_deposit(400)
an.make_deposit(150)

#Second User:Sydney
ok.make_withdrawal(150)
ok.make_withdrawal(160)
ok.make_deposit(205)
ok.make_deposit(290)

#Third User:Chris
get.make_deposit(700)
get.make_withdrawal(130)
get.make_withdrawal(100)
get.make_withdrawal(140)


an.display_user_balance()
ok.display_user_balance()
get.display_user_balance()