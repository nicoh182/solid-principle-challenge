import datetime

class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

        with open("transactions.log", "a") as log_file:
            log_file.write(
                f"{datetime.datetime.now()}: Deposited {amount} into {self.account_number}\n"
            )

        print(f"Sending email notification: {amount} deposited into account {self.account_number}.")

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount

        with open("transactions.log", "a") as log_file:
            log_file.write(
                f"{datetime.datetime.now()}: Withdrew {amount} from {self.account_number}\n"
            )

        print(f"Sending email notification: {amount} withdrawn from account {self.account_number}.")

    def generate_statement(self):
        statement = f"Statement for Account: {self.account_number}\nBalance: {self.balance}\n"

        print(statement)

        with open("statements.log", "a") as stmt_file:
            stmt_file.write(
                f"{datetime.datetime.now()}: Generated statement for {self.account_number}\n"
            )
        print(f"Sending email with statement for account {self.account_number}...")
