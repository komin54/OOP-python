class car:
    def __init__ (self, name, manufacturer, year):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
car1 = car("crv", "honda", 2017)

print(car1.name)
print(car1.manufacturer)
print(car1.year)
