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
    def viewbalance():
        return 0

class SavingsAccount(Account):
    def __init__(self):
        self.savingsAccount ={}
    def createAccount(self,name,initialDeposit):

        self.accountNumber=randint(10000,99999)
        self.savingsAccount[accountNumber]=[name,initialDeposit]
        print("ACCOUNT CREATED ,YOUR A/C NO IS",self.accountNumber)
    def authenticate(self,name,accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if self.savingsAccount[accountNumber][0]==name:
                print("AUTHENTICATION SUCCESSFUL")
                self.accountNumber=accountNumber
                return  True
            else:
                print("AUTHENTICATION FAILED")
                return  False
        else:
            print("AUTHENTICATION FAILED")
            return False
    def withdraw(self,withdrawAmount):
        if withdrawAmount>self.savingsAccount[self.accountNumber][1]:
            print("YOU DONT HAVE SUFFICIENT BALANCE")
        else:
            self.savingsAccount[self.accountNumber][1] -= withdrawAmount
            print("withdraw successful")
            self.viewbalance()
    def deposit(self,depositAmount):
        self.savingsAccount[self.accountNumber]=self.savingsAccount[self.accountNumber]+depositAmount
        print("DEPOSIT SUCCESSFUL")
        self.viewbalance()
    def viewbalance(self):
        print("THE BALANCE IN YOUR ACCOUNT IS",self.savingsAccount[self.accountNumber][1])
savingsAccount=SavingsAccount()
while True:
    print("Enter 1 to create account")
    print("Enter 2 to access existing account")
    print("Enter 3 to exit")
    choice=int(input())
    if choice==1:
        print("enter your name")
        name=input()
        print("enter your initial deposit")
        initialdeposit=int(input())
        savingsAccount.createAccount(name,initialdeposit)
    elif choice==2:
        print("enter the name")
        name=int()
        print("enter the account number")
        accountNumber=int(input())
        authenticationstatus=savingsAccount.authenticate(name,accountNumber)
        if authenticationstatus is True:
            print("enter 1 to withdraw")
            print("enter 2 to deposit")
            print("enter 3 to viewbalance")
            print("enter 4 to exit")
            choice=int(input())
            if choice==1:
                print("enter withdrawel amount")
                withdrawamount=int(input())
                savingsAccount.withdraw(withdrawamount)
            elif choice==2:
                print("enter deposit amount")
                Ideposit=int(input())
                savingsAccount.deposit(Ideposit)
            elif choice==3:
                print("view balance")
                savingsAccount.viewbalance()
            elif choice==4:
                break
    elif choice==3:
        quit()





