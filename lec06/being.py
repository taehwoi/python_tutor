class Being():
    """Top level generic class for all living things"""

    # Class Variables
    population = 0

    def __init__(self, name, hp, mp, race):
        # Object Variables
        self.name = name
        self.hp = hp
        self.mp = mp
        self.race = race

        Being.population += 1
        print("A new", race, "is born.")

    def die(self):
        self.hp = 0
        print(self.name, " is dead.")
        Being.population -= 1
        print(Being.population,
              "being is left standing on middle earth")


boss = Being("Smaug", 10, 5, "Dragon")
you = Being(name="Your Name", hp=10,
            mp=5, race="human")

boss.die()
