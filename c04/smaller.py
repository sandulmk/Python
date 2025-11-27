class Rectangle:
    def __init__(self, length, width):
        self.__length = length      
        self.__width = width        

    def area(self):
        return self.__length * self.__width

    
    def __lt__(self, other):
        return self.area() < other.area()



r1 = Rectangle(4, 5)
r2 = Rectangle(3, 10)

if r1 < r2:
    print("Rectangle r1 is smaller than r2")
else:
    print("Rectangle r1 is not smaller than r2")
