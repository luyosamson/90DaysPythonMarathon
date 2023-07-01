# Build a class called "BankAccount" with attributes like account number, 
# account holder name, and balance. Implement methods to deposit and withdraw money 
# from the account and calculate the interest earned over time.

class BankAccount:
    def __init__(self,ac_num,name,balance):
        self.ac_num=ac_num
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited {amount},Current balance is {self.balance}")

    def withdraw(self,amount):
         if amount<=self.balance:
          self.balance-=amount
          print(f"Amount withdrawn is {amount}.Current account balance is {self.balance}")
         else:
          print("Insufficient balance,kindly top up your account")
    def intrest(self,time ,rate):
       self.time=time
       self.rate=rate
       intrest=self.balance*time*rate/100
       print("Intrest is",intrest)

    def display_info(self):
       print("Account holder name",self.name)
       print("Account number",self.ac_num)
       print("Account balance",self.balance)
    
bank1=BankAccount("1236039971","Luyo",2000)
bal=bank1.deposit(500)
print(f"Current balance {bal}")
bank1.intrest(5,2)
bank1.withdraw(9000)

bank1.display_info()