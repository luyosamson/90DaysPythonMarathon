class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount > 5000:
         print("You can only deposit a minimum of 5000 a day")
        else:
         self.__balance += amount
  
       
    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
         self.__balance -= amount
        else:
           print("Insufficient balance")

bank1=BankAccount("1236039971Z",1000)
print(bank1.get_account_number())
print(bank1.get_balance())
bank1.deposit(900)
bank1.withdraw(10)
print(bank1.get_balance())



