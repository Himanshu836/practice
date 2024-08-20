# CREATE ACCOUNT CLASS WITH 2 ATTRIBUTES-BALANCE & ACC NO.CREATE METHOD FOR DEBIT,CREDIT,PRINT THE BALANCE

class Account:
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc
        print("your current balance is : ",self.bal)
    def debit(self,amount):
        self.bal=self.bal-amount
        print(f"Your {amount} was debited & your remaining balance is {self.bal}")
    def credit(self,amount):
        self.bal=self.bal+amount
        print(f"Your {amount} was credited & your current balance is {self.bal}")
    def balance(self):
        print(f"Your current amount is : {self.bal}")


user=Account(2500,12345)
user.debit(750)
user.credit(400)
user.balance()
