# Here your solution
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def fee(self, amount):
        return 0

class CreditCardPayment(PaymentMethod):
    def fee(self, amount):
        return amount * 0.03
    
class PayPalPayment(PaymentMethod):
    def fee(self, amount):
        return amount * 0.05

class BankTransferPayment(PaymentMethod):
    def fee(self, amount):
        return 2.50

class FeeCalculator:
    @staticmethod
    def calculate_fee(amount, payment_method: PaymentMethod):
        return payment_method.fee(amount)
