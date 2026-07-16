import random
from ability import Ability


class Weapon(Ability):
    def attack(self):
        ''' This method returns a random value
        between one half to the full attack power of the weapon.
        '''
        # Integer division to find half of max_damage
        half_damage = self.max_damage // 2
        return random.randint(half_damage, self.max_damage)


if __name__ == "__main__":
    test_weapon = Weapon("Sword", 40)
    print(test_weapon.name)
    print(test_weapon.attack())