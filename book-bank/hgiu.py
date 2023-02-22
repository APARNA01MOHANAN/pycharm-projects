
from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount():
        return 0

    @abstractmethod
    def authenticate():
        return 0

    @abstractmethod
    def withdraw():
        return 0

    @abstractmethod
    def deposit():
        return 0

    @abstractmethod
    def displayBalance():
        return 0


class SavingsAccount(Account):

    def __init__(self):
        # [key][0] = name; [key][1] = balance
        self.savingsAccount = {}

    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000,99999)
        self.savingsAccount[self.accountNumber] = [name,initialDeposit]
        print('Account created. Your a/c number is:', self.accountNumber)

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if self.savingsAccount[accountNumber][0] == name:
                print('Authentication is successfull!')
                self.accountNumber = accountNumber
                return True
            else:
                print('Authentication Failed!')
                return False
        else:
            print('Authentication Failed!')
            return False

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.savingsAccount[self.accountNumber][1]:
            print('Insufficient Balance')
        else:
            self.savingsAccount[self.accountNumber][1] -= withdrawlAmount
            print('Withdrawl Successful!')
            self.displayBalance()
    def deposit(self, depositAmount):
        self.savingsAccount[self.accountNumber][1] += depositAmount
        print('Deposit was successful!')
        self.displayBalance()

    def displayBalance(self):
        print('Balance in a/c:', self.savingsAccount[self.accountNumber][1])


savingsAccount = SavingsAccount()

# MENU CREATION:
while True:
    print('Enter 1 to create a new Account')
    print('Enter 2 to access an existing account')
    print('Enter 3 to exit')
    userChoice = int(input())
    if userChoice == 1:
        print('Enter your Name:')
        name = input()
        print('Enter Initial Deposit Account:')
        deposit = int(input())
        savingsAccount.createAccount(name,deposit)
    elif userChoice == 2:
        print('Enter your name:')
        name = input()
        print('Enter your A/C no:')
        accountNumber = int(input())
        autheticationStatus = savingsAccount.authenticate(name,accountNumber)
        if autheticationStatus is True:
            while True:
                print('Enter 1 to withdraw')
                print('Enter 2 to deposit')
                print('Enter 3 to display balance')
                print('Enter 4 to return to previous menu')
                userChoice = int(input())
                if userChoice == 1:
                    print('Enter withdrawl amount:')
                    withdrawlAmount = int(input())
                    savingsAccount.withdraw(withdrawlAmount)
                elif userChoice == 2:
                    print('Enter deposit amount:')
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)
                elif userChoice == 3:
                    savingsAccount.displayBalance()
                elif userChoice == 4:
                    break
    elif userChoice == 3:
        quit()