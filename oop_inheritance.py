



class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def  withdraw(self):
        print("**********To take withdraw******")
        amount=int(input("enter amount which you want  to withdraw:"))
        if amount<=self.balance:
            print("Withdraw  successfull---")
            self.balance-=amount
            print("Remaining blance is :",self.balance)
        else:
            print("your amount is very high .Ypur current balance is:",self.balance)
    def deposit(self):
        print("**********to deposit amount*****")
        amount=int(input("enter amount which you want to deposit:"))
        self.balance+=amount
        print("Your current balance is :",self.balance)
class SavingAccount(Account):
    def __init__(self,name,balance,interest_rate):
        super().__init__(name,balance)
        self.interest_rate=interest_rate
    def cal_interest(self):
            print("**********To calculate interest*********")
            t=int(input("enter time in year:"))
            interest=self.balance*self.interest_rate*t/100
            self.balance+=interest
            print("Interest is:",interest,"current balance with interest is:",self.balance)
a=SavingAccount("Hadia",10000,5)
a.withdraw()
a.deposit()
a.cal_interest()

