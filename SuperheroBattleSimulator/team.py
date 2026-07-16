import random


class Team:
    def __init__(self, name):
        '''Instance properties:
        name: String
        heroes: List
        '''
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, hero):
        if hero in self.heroes:
            self.heroes.remove(hero)

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def total_kills(self):
        '''Total kills across every hero on this team.'''
        total = 0
        for hero in self.heroes:
            total += hero.kills
        return total

    def total_deaths(self):
        '''Total deaths across every hero on this team.'''
        total = 0
        for hero in self.heroes:
            total += hero.deaths
        return total

    def attack(self, other_team):
        '''Randomly select a living hero from each team to fight.'''
        living_heroes = [h for h in self.heroes if h.is_alive()]
        living_opponents = [h for h in other_team.heroes if h.is_alive()]

        if not living_heroes or not living_opponents:
            return

        hero = random.choice(living_heroes)
        opponent = random.choice(living_opponents)
        hero.battle(opponent)

    def revive_heroes(self):
        '''Reset every hero on the team back to full health.'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health