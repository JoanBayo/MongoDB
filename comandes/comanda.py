class comanda:
    def __init__(self, id, idproducte, quantity, price):
        self.id = id
        self.idproducte = idproducte
        self.quantity = quantity
        self.price = price

    def totalprice(self):
        total = self.quantity * self.price
        print("total=" + str(total))
        return total
