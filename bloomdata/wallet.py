class Wallet:

    def __init__(self, initial_ammount=0):
        self.balence = initial_ammount

    def spend(self, amount):
        if amount >= self.balence:
            return 'not enough money'
        else:
            self.balence -= amount
            return f'${amount} spent, remaining balence: ${self.balence}'

    def deposit(self, amount):
        self.balence += amount
        return f'${amount} added, new balence: ${self.balence}'

    def __repr__(self):
        return f'Wallet with ballence: ${self.balence}'


if __name__ == '__main__':
    wallet1 = Wallet(100)
    print(wallet1.deposit(120))

    wallet2 = Wallet()
    print(wallet2)
