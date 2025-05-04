import random

class Tiger:
    def __init__(self):
        self.state = "hunting"
        self.lucky = 0.5
        self.x = 0, 0
        self.y = 0, 0

class Rabbit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        is_catched = False

    def to_catch(self):
        self.is_catched = True

class Field:
    def __init__(self, tiger, rabbits):
        self.size = 5
        grid = []
        for i in range(5):
            row = []
            for i in range(5):
                row.append("*")
            grid.append(row)
