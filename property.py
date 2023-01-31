class Property:
    def __init__(self, name, value, house_cost=None, hotel_cost=None, mortgage=None, tax=None):
        self.name = name
        self.value = value

        self.house_cost = house_cost if house_cost is not None else 50.0
        self.hotel_cost = hotel_cost if hotel_cost is not None else 200.0
        self.mortgage = mortgage if mortgage is not None else 50.0

        self.tax = tax if tax is not None else [10.0, 20.0, 50.0, 140.0, 250.0, 500.0]
        self.infrastructure = 0

        self.bought = True

    def get_tax(self):
        return self.tax[self.infrastructure]

    def buy_infrastructure(self, money):
        if not self.bought:
            return False
        elif self.infrastructure == 5:
            return False
        elif self.infrastructure == 4 and money < self.hotel_cost:
            return False
        elif money < self.house_cost:
            return False
        else:
            self.infrastructure += 1
            return True

    def buy(self, money):
        if not self.bought and money >= self.value:
            self.bought = True
            return True
        else:
            return False