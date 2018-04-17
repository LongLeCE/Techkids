class Car:
    brand = "Not set"
    maxSpeed = "Not set"

    @classmethod
    def set_brand(cls, b):
        cls.brand = b

    @classmethod
    def set_maxspeed(cls, m):
        cls.maxSpeed = "".join(x for x in [str(m), " km/h"])

    def print_data(self):
        print("Brand:", self.brand, "\nMax Speed:", self.maxSpeed)


Car().print_data()
Car().set_brand("Audi")
Car().set_maxspeed(200)
Car().print_data()
