# parent class is moree generic
class Vehicle:

    def __init__(self, make, model, color, year, milage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.milage = milage

    def honk(self):
        return "Beep Beep!"

    def drive(self, miles):
        self.milage += miles
        return self.milage

    def __repr__(self):
        return f'''{self.color}, {self.year} {self.make}
        {self.model} with {self.milage} miles'''


if __name__ == "__main__":
    carl = Vehicle("Honda", "CR-V", 'blue', '2009', 175000)
    print(carl)


# child class is more specific
class Convertible(Vehicle):

    def __init__(self, make, model, color, year, milage, top_down=True):
        super().__init__(make, model, color, year, milage)
        self.top_down = top_down


conv = Convertible('toyota', 'prius', 'pink', '2024', 0)
print(conv.honk())
