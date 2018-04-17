class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()

    def order(self, food_name):
        self.customer.place_order(food_name)

    def receipt(self):
        return self.employee.food_ordered()


class Customer:

    @classmethod
    def place_order(cls, food_name):
        cls.food_name = Employee().take_order(food_name)


class Employee:
    @staticmethod
    def take_order(food_name):
        return Food(food_name).name

    @staticmethod
    def food_ordered():
        return Customer().food_name


class Food:
    def __init__(self, name):
        self.name = name


x = Lunch()
x.order("Lobster")
print(x.receipt())
