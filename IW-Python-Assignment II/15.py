# 15. Imagine you are designing a banking application. What would a customer look like? What attributes would she
# have? What methods would she have?


class Customer:

    def __init__(self,c_id,name,account_no,balance):
        self.c_id = c_id
        self.name = name
        self.account = account_no
        self.balance = balance

    def get_info(self, c_id):
        return self.name,self.account,self.balance

    def diposit(self, amount):
        self.balance += amount
        print("Successful diposit of Rs.{}".format(amount))
        print("Current balance is Rs.{}".format(self.balance))

    def withdrawl(self, amount):
        if self.balance < amount:
            print("Yo do not have enough balance. Please try less amount")

        else:
            self.balance -= amount
            print("You had successful withdrawl of Rs.{}.".format(amount))
            print("Current balance is Rs.{}".format(self.balance))

customer_1 = Customer(1, 'Sarita Thapa',34534, 150000)

name, account_no, balance = customer_1.get_info(1)
print(" Name : {}\n".format(name), "Account no: {}\n".format(account_no), "Balance : Rs.{}\n".format(balance))

customer_1.diposit(23000)
customer_1.withdrawl(5000)
