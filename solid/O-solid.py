class FeeCalculator:
    @staticmethod
    def calculate_fee(amount, payment_method):
        """
        Violates OCP because every new payment method 
        (e.g., 'CRYPTO', 'WIRE_TRANSFER') requires modifying this method.
        """
        if payment_method == "CREDIT_CARD":
            # 3% fee
            return amount * 0.03
        elif payment_method == "PAYPAL":
            # 5% fee
            return amount * 0.05
        elif payment_method == "BANK_TRANSFER":
            # Flat fee of 2.50
            return 2.50
        else:
            # Unknown method, no fee
            return 0.0