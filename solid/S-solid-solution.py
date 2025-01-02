# Here your solution
import datetime

class NotificationService:
    def __init__(self):
        pass

    @staticmethod
    def notify(type, amount, account_number):

        with open("transactions.log", "a") as log_file:
            log_file.write(
                f"{datetime.datetime.now()}: {type} {amount} into {account_number}\n"
            )

        print(f"Sending email notification: {amount} {type} into account {account_number}.")

class DepositService:
    def __init__(self, account):
        self.account = account

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.account.balance += amount
        
        NotificationService.notify("deposit", amount, self.account.account_number)

class WithdrawService:
    def __init__(self, account):
        self.account = account

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.account.balance:
            raise ValueError("Insufficient funds.")

        self.account.balance -= amount

        NotificationService.notify("withdrawn", amount, self.account.account_number)

class GenerateStatementService:
    def __init__(self):
        pass

    def generate_statement(self):
        statement = f"Statement for Account: {self.account.account_number}\nBalance: {self.account.balance}\n"

        print(statement)

        with open("statements.log", "a") as stmt_file:
            stmt_file.write(
                f"{datetime.datetime.now()}: Generated statement for {self.account.account_number}\n"
            )
        print(f"Sending email with statement for account {self.account.account_number}...")

class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance
