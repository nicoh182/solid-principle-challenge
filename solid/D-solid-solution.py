# Here your solution
from abc import ABC, abstractmethod

class IntefacePayService(ABC):
    @abstractmethod
    def pay(amount: float):
        pass

class PayPalService(IntefacePayService):
    @staticmethod
    def pay(amount: float):
        print(f"Paying {amount} using PayPal...")

class PaymentProcessor:
    def process_payment(self, pay_service: IntefacePayService, amount: float):
        pay_service.pay(amount)
