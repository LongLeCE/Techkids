class Rectangle:
    def __init__(self, h, w):
        self.height = h
        self.width = w

    def area(self):
        return self.height * self.width


print(Rectangle(200, 20).area())
