import random


class Armor:
    def __init__(self, name, max_block):
        '''Instance properties:
        name: String
        max_block: Integer
        '''
        self.name = name
        self.max_block = int(max_block)

    def block(self):
        '''Returns a random value between 0 and max_block.'''
        return random.randint(0, self.max_block)


if __name__ == "__main__":
    test_armor = Armor("Shield", 20)
    print(test_armor.name)
    print(test_armor.block())