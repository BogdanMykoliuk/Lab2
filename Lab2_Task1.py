class Rectangle:
    def __init__(self, width=1, length=1):
        self.width = width
        self.length = length

    def set_length(self, length):
        if isinstance(length, (float, int)) and length > 0.0 and length <= 20.0:
            self.length = length
        else:
            self.error()
            return None

    def set_width(self, width):
        if isinstance(width, (float, int)) and width > 0.0 and width <= 20.0:
            self.width = width
        else:
            self.error()
            return None

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def calculate(self):
        return "Perimeter: " + str((self.width + self.length) * 2) + "\n" + "Area:" + str(self.width * self.length)

    def error(self):
        print("ERROR")


x = Rectangle(5, 9)
print(x.calculate())

