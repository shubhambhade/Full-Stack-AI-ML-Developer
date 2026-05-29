class BankAccount:

    def __init__(self, account_holder, balance):

        self.account_holder = account_holder

        # Private Variable
        self.__balance = balance

    # Deposit Method
    def deposit(self, amount):

        if amount <= 0:
            print("Invalid deposit amount")
            return

        self.__balance += amount

        print(f"₹{amount} deposited successfully")

    # Withdraw Method
    def withdraw(self, amount):

        if amount > self.__balance:
            print("Insufficient Balance")
            return

        self.__balance -= amount

        print(f"₹{amount} withdrawn successfully")

    # Getter Method
    def get_balance(self):

        return self.__balance

# Create Object
account = BankAccount("Shubham", 50000)

# Deposit
account.deposit(10000)

# Withdraw
account.withdraw(5000)

# Access Balance
print("Current Balance :", account.get_balance())