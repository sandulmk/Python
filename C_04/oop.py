class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimetr(self):
        return 2 * (self.length + self.breadth)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

r1 = Rectangle(4, 5)
r2 = Rectangle(3, 10)

print("Area of r1:", r1.area())
print("Area of r2:", r2.area())

if r1 < r2:
    print("r2 is larger than r1")
elif r1 == r2:
    print("Both rectangles have the same area")
else:
    print("r1 is larger than r2")
