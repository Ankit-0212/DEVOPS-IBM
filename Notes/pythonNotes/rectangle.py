from shape import Shape
class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__(width,height)

    def area(self):
        return self._width*self._height