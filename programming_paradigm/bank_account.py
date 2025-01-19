class BankAccount:
    def __init__(self, balance = 0):
        self.Account_balance = balance
        
    def deposit(self,amount):
        self.Account_balance += amount
        return self.Account_balance
            
    def withdraw(self,amount):
        if self.Account_balance > amount:
            self.Account_balance -= amount
            return self.Account_balance
            
    def display_balance(self,amount):
        return f"Your Account balance is: ${self.Account_balance}"
        

  