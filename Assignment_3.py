from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card ({self.card_holder}, {self.card_number}).")


class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid {amount} using PayPal account ({self.email}).")


class UPIPayment(PaymentStrategy):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Paid {amount} using UPI ID ({self.upi_id}).")


# Context
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        """Dynamically change payment method"""
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Example Usage
if __name__ == "__main__":
    # Start with Credit Card
    processor = PaymentProcessor(CreditCardPayment("1234-5678-9876", "Alice"))
    processor.process_payment(500)

    # Switch to PayPal
    processor.set_strategy(PayPalPayment("alice@example.com"))
    processor.process_payment(750)

    # Switch to UPI
    processor.set_strategy(UPIPayment("alice@upi"))
    processor.process_payment(300)
