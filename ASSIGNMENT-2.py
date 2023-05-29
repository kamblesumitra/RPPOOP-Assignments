class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = [0] * num_sides

    def input_sides(self):
        self.sides = [float(input(f"Enter side {i+1}: ")) for i in range(self.num_sides)]

    def perimeter(self):
        return sum(self.sides)

    def report_sides(self):
        return f"Sides: {', '.join(str(side) for side in self.sides)}"


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)

    def area(self):
        return self.sides[0] * self.sides[1]


class Square(Rectangle):
    def __init__(self):
        super().__init__()

    def area(self):
        return self.sides[0] ** 2


# Testing the classes
rectangle = Rectangle()
rectangle.input_sides()
print(rectangle.report_sides())
print("Perimeter:", rectangle.perimeter())
print("Area:", rectangle.area())

square = Square()
square.input_sides()
print(square.report_sides())
print("Perimeter:", square.perimeter())
print("Area:", square.area())
