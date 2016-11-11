# Nikolei Advani, 11/11/16
# This program tests the account class.

import account


def firstAccount():
    nikolei = account.Account("Nikolei", 12345, 150)
    nikolei.withdraw(50)
    print(nikolei.showBalance())
    if nikolei.withdraw(110):
        print(nikolei.showBalance())
    else:
        print("Invalid balance")
    nikolei.deposit(200)
    print(nikolei.showBalance())
    nikolei.deposit(50)
    print(nikolei.showBalance())
    print(nikolei)


def secondAccount():
    james = account.Account("James", 67890, 100)
    james.deposit(200)
    print(james.showBalance())
    james.withdraw(20)
    print(james.showBalance())
    if james.withdraw(200):
        print(james.showBalance())
    else:
        print("Invalid balance")
    james.deposit(50)
    print(james.showBalance())
    print(james)


def thirdAccount():
    chiedu = account.Account("Chiedu", 7410, 50)
    chiedu.deposit(50)
    print(chiedu.showBalance())
    chiedu.deposit(150)
    print(chiedu.showBalance())
    if chiedu.withdraw(450):
        chiedu.showBalance()
    else:
        print("Invalid balance")
    chiedu.withdraw(25)
    print(chiedu.showBalance())
    print(chiedu)


def main():
    firstAccount()
    secondAccount()
    thirdAccount()

main()


