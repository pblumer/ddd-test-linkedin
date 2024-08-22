class Checkout:
    class Discount:
        def __init__(self, quantity, price):
            self.quantity = quantity
            self.price = price
        
    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}
        self.total = 0
    
    def addDiscount(self, item, quantity, price):
        discount = self.Discount(quantity, price)
        self.discounts[item] = discount

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, count in self.items.items():
            total += self.calculateItemTotal(item, count)
        
        return total
    

    def calculateItemTotal(self, item, count):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.quantity:
                total += self.calculateDiscountedTotal(item, count, discount)
            else:
                    total += self.prices[item] * count
        else:
            total += self.prices[item] * count

        return total
    
    def calculateDiscountedTotal(self, item, count, discount):
        total = 0
        numberOfDiscounts = count / discount.quantity
        total += numberOfDiscounts * discount.price
        remaining = count % discount.quantity
        total += remaining * self.prices[item]
        return total