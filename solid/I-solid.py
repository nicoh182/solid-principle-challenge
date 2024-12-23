from abc import ABC, abstractmethod

class IPaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

    @abstractmethod
    def refund(self, amount: float) -> None:
        pass

    @abstractmethod
    def handle_dispute(self, dispute_id: str) -> None:
        pass


class BasicGiftCard(IPaymentGateway):
    def pay(self, amount: float) -> None:
        print(f"Gift card used to pay {amount}.")

    def refund(self, amount: float) -> None:
        raise NotImplementedError("Gift cards do not support refunds.")

    def handle_dispute(self, dispute_id: str) -> None:
        raise NotImplementedError("Gift cards do not support disputes.")
