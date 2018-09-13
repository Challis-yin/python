class car():
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def add(self,adds):
        self.age += adds
    def show(self):
        print(self.name+"   "+str(self.age))
CAR = car("benchi", 13)
CAR.show()
CAR.add(35)
CAR.show()