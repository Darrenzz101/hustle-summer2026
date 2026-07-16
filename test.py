class animal:
    def __init__(self, legs, fur, colors, lifespan, eyes, habitat, size):
        self.legs = legs
        self.fur = fur
        self.colors = colors
        self.lifespan = lifespan
        self.eyes = eyes
        self.habitat = habitat
        self.size = size

    def move(self):
        if self.legs >= 2:
            print("ZOOOOM")
        elif self.legs == 1:
            print("Hop hop hop")
        else:
            print("I can't move!")

