# Here your solution
class PaymentMethodInterface:
    def __init__(self, balance: float):
        self.balance = balance

class PaymentMethod(PaymentMethodInterface):
    def __init__(self, balance: float):
        super().__init__(balance)

    def pay(self, amount: float):
        if amount > self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= amount
        print(f"[PaymentMethod] Paid {amount}. New balance: {self.balance}")

    def refund(self, amount: float):
        self.balance += amount
        print(f"[PaymentMethod] Refunded {amount}. New balance: {self.balance}")


class NonRefundableGiftCard(PaymentMethodInterface):
    def __init__(self, balance):
        super().__init__(balance)

    def refund(self, amount: float):
        raise NotImplementedError(
            "NonRefundableGiftCard does not support refunds."
        )
