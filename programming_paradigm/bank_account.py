class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited {amount}: The new balance is {self.__account_balance}")
        else:
            print("The amount must be greater than zero!")
    
    def withdraw(self, amount):
        if amount > 0 and self.__account_balance >= amount:
            self.__account_balance -= amount
            print(f"Withdrawing {amount}: The new balance is {self.__account_balance}")
            return True
        elif amount > self.__account_balance:
            print("Insufficient Funds! You account does not have enough money.")
            return False

        else:
            print("The amount must be greater than zero!")
            return False
            
    def display_balance(self):
        print(f"Current balance: ${self.__account_balance}")


