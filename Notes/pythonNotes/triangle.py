from shape import Shape
class Triangle(Shape):
    def __init__(self,width,height):
        super().__init__(width,height)

    def area(self):
        return 0.5*self._width*self._height