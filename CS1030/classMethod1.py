import datetime
import pytz

class Account(object):

    def __init__(self, name, balance):
        #superAccount, self).__init__()
        self.name = name
        self.balance = balance
        self.transaction = transaction_list = []
        print("Account created for: " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance+= amount
            self.transaction_list.append(pytz.utc.localize(datetime.datetime.utcnow()),amount)
            self.showBalance()
    def withdraw(self, amount):
        if 0 <= amount < self.balance:
            self.balance -= amount
        else:
            print("The Amout must be greater than Zero. ")
        self.showBalance()
    def showBalance(self):
        print("balance is {}".format(self.balance))
    def transaction_list(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                trans_type = "Deposted"
            else:
                trans_type = "withdraw"
                amount*= -1
            print("{:6} {} on {} (local time was {})".format(amount, trans_type, date, date.astimezone()))

if __name__ == '__main__':
    abi = Account("Abinet", 0)
    print("After 1st deposit")
    abi.deposit(1000)
    print("After 1st withdraw")
    abi.withdraw(1500)
