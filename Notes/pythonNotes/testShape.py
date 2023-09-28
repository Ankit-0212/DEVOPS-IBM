from shape import Shape
from rectangle import Rectangle
from triangle import Triangle


class Main:
    @staticmethod
    def display(shape):
        return shape.area()



print(Main.display(Rectangle(2,4)))
print(Main.display(Triangle(10,2)))