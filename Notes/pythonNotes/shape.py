class Shape:
    def __init__(self,width,height):
        self._width = width
        self._height = height
    def __subclasscheck__(self, subclass):
        return hasattr(subclass,'area') and callable(subclass.area)