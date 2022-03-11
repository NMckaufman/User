class User:
    def __init__(self,name):
        self.name = name
        self.balance = 0
    
    def make_deposit(self,amount):
        self.balance += amount
        return self

    def make_withdrawal(self,amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print (f"Name:{self.name} Balance:{self.balance}")
        return self

    def transfer_money(self,amount,second_party):
        self.balance -= amount
        second_party.balance += amount
        self.display_user_balance()
        second_party.display_user_balance()
        return self



Mikail = User("Mikail")
Kaiyah = User("Kaiyah")
Amal = User("Amal")


Mikail.make_deposit(250).make_deposit(56).make_deposit(23).make_withdrawal(43).display_user_balance().transfer_money(64, Amal)

Kaiyah.make_deposit(113).make_deposit(237).make_withdrawal(34).display_user_balance()

Amal.make_deposit(241).make_withdrawal(22).make_withdrawal(13).make_withdrawal(4).display_user_balance()