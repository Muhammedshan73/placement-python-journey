class BankAccount:
    def __init__(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self._balance=balance
    def deposit(self,amount):
        self._balance+=amount
        return self._balance
    def withdraw(self,amount):
        if amount<=self._balance:
            self._balance -= amount
            return self._balance
        else:
            return "Insufficiant Balance"
    def get_Balance(self):
        return self._balance
    def calculate_intrest(self):
        pass

class SavingAccount(BankAccount):
    def calculate_intrest(self):
        intrest = self._balance*0.04
        return intrest

class CurrentAccount(BankAccount):
    def calculate_intrest(self):
        return 0
class BankApp:
    def __init__(self):
        self.account=None
    def create_account(self,acc_no,name,balance,acc_type):
        if acc_type=="savings":
            self.account=SavingAccount(acc_no,name,balance)
        else:
            self.account=CurrentAccount(acc_no,name,balance)
        return "Account created Succesfully"
    def deposit_money(self,amount):
        return self.account.deposit(amount)
    def withdraw_money(self,amount):
        return self.account.withdraw(amount)
    def check_balance(self):
        return self.account.get_Balance()
    def get_interest(self):
        return self.account.calculate_intrest()

App = BankApp()
print(App.create_account(101,"Rahul",10000,"savings"))
print("balance after deposit:",App.deposit_money(2000))
print("balance after withdraw:",App.withdraw_money(2000))
print("Current balance:",App.check_balance())
print("Interest is",App.get_interest())
