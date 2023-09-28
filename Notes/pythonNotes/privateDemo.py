class Base:
    def myFunc(self):
        print("This is a public function")
    def __myFunc(self):
        print("this is a private function")



class Derived(Base):
    def __init__(self):
        Base.__init__(self)
    def callPublic(self):
        self.myFunc()
    def callPrivate(self):
        self.__myFunc()

def __printFun():
    print("hello there")
obj1 = Base()
obj1.myFunc()
# obj1.__myFunc()


obj2 = Derived()
obj2.callPublic()
# obj2.callPrivate()
__printFun()
