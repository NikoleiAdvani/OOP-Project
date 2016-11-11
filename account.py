# Nikolei Advani, 11/11/16
# This class creates a framework for a basic bank account.


class Account:
    balance = 0

    def __init__(self, name, accountNumber, balance):
        """This class includes the name under the account, the account number, and the account balance."""
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, amount):
        """This definition makes account deposists"""
        self.balance += amount

    def withdraw(self, amount):
        """This definition makes account withdrawls. This if statement restricts withdrawl if the amount exceeds user's balance"""
        if amount < self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def showBalance(self):
        """This definition shows the account balance"""
        return self.balance

    def __str__(self):
        """This definition prints the account information to the user"""
        return self.name + "'s account balance is " + str(self.balance)
