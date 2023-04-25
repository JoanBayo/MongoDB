class comanda:
    def __init__(self, id, quantity, price):
        self.id = id
        self.quantity = quantity
        self.price = price

    def totalprice(self):
        total = self.quantity * self.price
        print("total=" + str(total))
        return total
