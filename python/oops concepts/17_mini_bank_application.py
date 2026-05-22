class Customer:
    '''this application for banking system'''
    bank_name = "SBI Bank"
    def __init__(self,name, balance = 0.0):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f'After deposit balance is {self.balance}')
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient funds.....can't perform this operation")
        else:
            self.balance -= amount
            print("After withdraw balance : ",self.balance)

print("Welcome to ", Customer.bank_name)
name = input("Enter your name : ")
customer = Customer(name)

while True:
    print('d- deposit\nw-withdraw\ne-exit')
    option = input('choose your option : ')
    if option.lower() == 'd':
        amount = float(input("Enter amount to deposit : "))
        customer.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input("enter amount to withdraw : "))
        customer.withdraw(amount)
    elif option.lower() == 'e':
        print("Thanks for banking")
        break
    else:
        print("your option is invalid please select valid option")
