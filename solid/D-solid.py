class PayPalService:
    @staticmethod
    def pay(amount: float):
        print(f"Paying {amount} using PayPal...")


class PaymentProcessor:
    def __init__(self):
        self.paypal_service = PayPalService()

    def process_payment(self, amount: float):
        self.paypal_service.pay(amount)

