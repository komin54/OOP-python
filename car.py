class car:
    def __init__ (self, name, manufacturer, year):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
car1 = car("crv", "honda", 2017)
car2 = car("gtr", "bmw", 2001)
car3 = car("rx-8", "mazda", 20002)

 data1 = Car()
if isinstance(data1, Car):
    print(f"data1 class inherit from Car")
if isinstance(data1, object):
    print(f"data1 class inherit from object")

data2 = "Noval Agung"
if isinstance(data2, str):
    print(f"data2 class inherit from str")
if isinstance(data2, object):
    print(f"data2 class inherit from object")