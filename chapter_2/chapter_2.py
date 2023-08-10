
class Dollar():
    def __init__(self, amount) -> None:
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def equals(self, obj):
        return self.amount == obj.amount
