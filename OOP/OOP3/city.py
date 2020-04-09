class City:

    def __init__(self, name, pop, area, mayor, teams=[]):   
        self.name = name
        self.population = pop
        self.size = area
        self.mayor = mayor
        self.sport_teams = teams

    def __eq__(self, other_city):
        return self.population == other_city.population and self.mayor[0] == other_city.mayor[0]

    def __str__(self):
        if len(self.sport_teams) == 0:
            return f'{self.name} city has {self.population} people, {self.size} area. Mayor is {self.mayor}. This city has no sport team.'
        else:
            teams = ', '.join(self.sport_teams) 
            return f'{self.name} city has {self.population} people, {self.size} area. Mayor is {self.mayor}. This city has {teams}.'
    
    def build_team(self, team):
        

boston = City('Boston', 6, 10, 'Walsh', ['Celtics', 'Patriots'])
ny = City('New York', 6, 100, 'Wuomo')

print(boston)
print(ny)

print(boston == ny)


