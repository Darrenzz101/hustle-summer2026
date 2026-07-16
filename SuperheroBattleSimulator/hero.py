import random
from ability import Ability
from armor import Armor


class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
        armors: List
        abilities: List
        kills: Integer
        deaths: Integer
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.armors = []
        self.abilities = []
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        '''Append an ability to this hero's list of abilities.'''
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        '''Weapons act just like abilities in a fight, so they go
        into the same abilities list.'''
        self.abilities.append(weapon)

    def add_armor(self, armor):
        '''Append armor to this hero's list of armors.'''
        self.armors.append(armor)

    def add_kill(self):
        self.kills += 1

    def add_death(self):
        self.deaths += 1

    def attack(self):
        '''Loop through abilities/weapons and sum their attack values.'''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        '''Loop through armors and sum their block values.'''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        '''Reduce current_health based on incoming damage minus
        whatever the hero's armor blocks.'''
        blocked = self.defend()
        net_damage = damage - blocked
        if net_damage > 0:
            self.current_health -= net_damage

    def is_alive(self):
        return self.current_health > 0

    def battle(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in.'''
        if not self.abilities or not opponent.abilities:
            print("Draw")
            return

        while self.is_alive() and opponent.is_alive():
            opponent.take_damage(self.attack())
            if not opponent.is_alive():
                break
            self.take_damage(opponent.attack())

        if self.is_alive() and not opponent.is_alive():
            print(self.name + " won!")
            self.add_kill()
            opponent.add_death()
        elif opponent.is_alive() and not self.is_alive():
            print(opponent.name + " won!")
            opponent.add_kill()
            self.add_death()
        else:
            print("Draw")


if __name__ == "__main__":
    my_hero = Hero("Spider-Man", 150)
    my_opponent = Hero("Venom", 200)

    my_hero.add_ability(Ability("Web Shooters", 25))
    my_opponent.add_ability(Ability("Symbiote Slam", 30))

    my_hero.battle(my_opponent)