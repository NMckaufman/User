class User:
    def __init__(self,name):
        self.name = name
        self.balance = 0
    
    def make_deposit(self,amount):
        self.balance += amount

    def make_withdrawal(self,amount):
        self.balance -= amount

    def display_user_balance(self):
        print (f"Name:{self.name} Balance:{self.balance}")

    def transfer_money(self,amount,second_party):
        self.balance -= amount
        second_party.balance += amount
        self.display_user_balance()
        second_party.display_user_balance()



Mikail = User("Mikail")
Kaiyah = User("Kaiyah")
Amal = User("Amal")


Mikail.make_deposit(250)
Mikail.make_deposit(56)
Mikail.make_deposit(23)
Mikail.make_withdrawal(43)
Mikail.display_user_balance()
Mikail.transfer_money(64, Amal)

Kaiyah.make_deposit(113)
Kaiyah.make_deposit(237)
Kaiyah.make_withdrawal(34)
Kaiyah.display_user_balance()

Amal.make_deposit(241)
Amal.make_withdrawal(22)
Amal.make_withdrawal(13)
Amal.make_withdrawal(4)
Amal.display_user_balance()





