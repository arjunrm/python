class BankAccount():
    minBalance = 1000

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposited: {}, Total Balance: {}".format(amount, self.balance))
    
    def withDraw(self, amount):
        if ((self.balance - amount) < BankAccount.minBalance):
            print("Not enough funds to withdraw")
        else:
            self.balance -= amount
            print("Withdrawn: {}, Total Balance: {}".format(amount, self.balance))

    def __str__(self):
        return ("Account holder: {}, Balance: {}".format(self.owner, self.balance))

if __name__ == '__main__':
    a1 = BankAccount("Arjun", 5000)
    s1 = BankAccount("Shravani", 10000)

    a1.deposit(1000)
    a1.withDraw(5500)
    print(a1)

    s1.withDraw(300)
    print(s1)

    myList = []
    help(myList)