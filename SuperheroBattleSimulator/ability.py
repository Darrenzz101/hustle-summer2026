import random


class Ability:
    def __init__(self, name, max_damage):
        '''Instance properties:
        name: String
        max_damage: Integer
        '''
        self.name = name
        self.max_damage = int(max_damage)

    def attack(self):
        '''Returns a random value between 0 and max_damage,
        so the hero doesn't hit for the exact same amount every time.
        '''
        return random.randint(0, self.max_damage)


if __name__ == "__main__":
    test_ability = Ability("Fireball", 30)
    print(test_ability.name)
    print(test_ability.attack())