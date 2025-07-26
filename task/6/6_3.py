"""
Task 6.3: Encapsulation

Create a class BankAccount with:

✔ Private attribute __balance
✔ Method to deposit and withdraw (with validation)
✔ Method to check balance
✔ Demonstrate access to private variable via methods only
"""
class bank:
    def __init__(self,initial_amount=0):
        self.__balence=initial_amount
    def check_balence(self):
        print(f"Your balence is : {self.__balence}")
    def deposite(self,amount):
        if amount>0:
            self.__balence+=amount
            print(f"{amount} is added to your account")
        else:
            print("the amount must be greater than zero")
    def withdraw(self,amount):
        if amount>self.__balence:
            print("insufficieant balence")
        elif amount <0:
            print("invalid amount")
        else:
            self.__balence-=amount
            print(f"{amount} withdrawn successfully")            
user_1=bank()
user_1.check_balence()
user_1.deposite(500)
user_1.deposite(-3)
user_1.withdraw(5001)
user_1.withdraw(50)
user_1.withdraw(-67)