import random


class Product:
    '''

    '''
    id = random.randint(1000000, 9999999)

    def __init__(self, name, price=10, weight=20,
                 flammability=0.5, identifier=id):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        steal = self.price / self.weight
        if steal < 0.5:
            return "Not so stealable..."
        if 0.5 <= steal < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        splode = self.flammability * self.weight
        if splode < 10:
            return "...fizzle."
        if 10 <= splode < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"

    def __repr__(self):
        return f'''{self.identifier}, name: {self.name}, price: {self.price},
                weight: {self.weight}, flammability: {self.flammability}'''


class BoxingGlove(Product):
    '''

    '''

    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=id):
        super().__init__(name, price, identifier)
        self.weight = weight
        self.flammability = flammability

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        if 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"


bg1 = BoxingGlove("yeet")
uno = Product('uno')
if __name__ == "__main__":
    print(bg1.flammability)
