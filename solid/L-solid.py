class PaymentMethod:
    def __init__(self, balance: float):
        self.balance = balance

    def pay(self, amount: float):
        if amount > self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= amount
        print(f"[PaymentMethod] Paid {amount}. New balance: {self.balance}")

    def refund(self, amount: float):
        self.balance += amount
        print(f"[PaymentMethod] Refunded {amount}. New balance: {self.balance}")


class NonRefundableGiftCard(PaymentMethod):
    def refund(self, amount: float):
        raise NotImplementedError(
            "NonRefundableGiftCard does not support refunds."
        )