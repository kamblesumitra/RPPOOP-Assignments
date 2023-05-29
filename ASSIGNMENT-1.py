class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def change_dimensions(self, new_length, new_width):
        self.length = new_length
        self.width = new_width

    def report_dimensions(self):
        return f"Length: {self.length}, Width: {self.width}"


# Testing the Rectangle class
rectangle = Rectangle(5, 3)
print("Area:", rectangle.area())  # Output: 15
print("Perimeter:", rectangle.perimeter())  # Output: 16
print(rectangle.report_dimensions())  # Output: Length: 5, Width: 3

rectangle.change_dimensions(7, 4)
print(rectangle.report_dimensions())  # Output: Length: 7, Width: 4

print("Area:", rectangle.area())  # Output: 28
print("Perimeter:", rectangle.perimeter())  # Output: 22
