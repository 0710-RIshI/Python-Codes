class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    
    def deposit(self,value):
        self.balance=value + self.balance
        print(f"deposited successfully and the total balance is {self.balance}")
    def withdraw(self,value):
        if(self.balance<value):
            print("insufficient balance")
        else:
            self.balance = self.balance - value
            print(f"money debited successfully the available balance is {self.balance}")


a = Account("rishi",1000)
a.deposit(10000)
a.withdraw(12000)
a.withdraw(1000)



    
