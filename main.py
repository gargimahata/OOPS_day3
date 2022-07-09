class car:      #parent class

    def __init__(self, body, engin, tyre):
        self.body = body
        self.engin = engin
        self.tyre = tyre

    def milage (self):
        print("milage of this car")

c = car("sold", "v6", "radial")
print(c)

class tata(car):      #child class
    pass

t = tata("solid2", "v8", "radial2")
print(t)
print(t.milage())
