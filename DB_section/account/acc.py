class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw (self, amount):
        self.balance = self.balance - amount
    def deposit(self, amount):
        self.balance = self.balance + amount
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):

    def __init__(self,filepath, fee):
        Account.__init__(self,filepath)
        self.fee = fee

    def transfer(self,amount):
        self.balance = self.balance -amount - self.fee

checking = Checking("account\\balance.txt",1)
checking.transfer(100)
checking.commit()
