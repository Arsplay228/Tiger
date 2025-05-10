import random

class Tiger:
    def __init__(self):
        self.state = "hunting"
        self.lucky = 0.5
        self.x = 0
        self.y = 0

    def move_randomly(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])
        self.x = max(0, min(self.x, 4))
        self.y = max(0, min(self.y, 4))
        print(self.x, self.y)

    def dispatch_mode(self, list_rabbits):
        if self.state == "hunting":
            print("Тигр охотится!")
            self.move_randomly()

            if any(self.is_near_rabbit(rabbit) for rabbit in list_rabbits):
                self.state = "attack"

        if self.state == "attack":
            print("Тигр перешёл в состояние атаки!")


    def is_near_rabbit(self, rabbit):
        return abs(self.x - rabbit.x) <= 1 and abs(self.y - rabbit.y) <= 1

class Rabbit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_catched = False

    def to_catch(self):
        self.is_catched = True

class Field:
    def __init__(self, tiger, rabbits):
        self.size = 5
        self.tiger = tiger
        self.rabbits = rabbits
        self.grid = []
        self.update_display()

    def update_display(self):
        self.grid = []

        for i in range(5):
            row = []
            for j in range(5):
                row.append("*")
            self.grid.append(row)

    def display(self):
        self.grid[self.tiger.x][self.tiger.y] = "T"
        for rabbit in self.rabbits:
            if not rabbit.is_catched:
                self.grid[rabbit.x][rabbit.y] = "З"

        for row in self.grid:
            line = ""
            for cell in row:
                line += cell + " "
            print(line)

class Game:
    def __init__(self):
        self.tiger = Tiger()
        self.rabbit_first = Rabbit(random.randint(1, 4), random.randint(1, 4))
        self.rabbit_second = Rabbit(random.randint(1, 4), random.randint(1, 4))
        self.list_rabbits = [self.rabbit_first, self.rabbit_second]
        self.field = Field(self.tiger, self.list_rabbits)
        self.game_loop()

    def game_loop(self):
        while self.tiger.state != "Go home":
            self.tiger.dispatch_mode(self.list_rabbits)
            self.field.update_display()
            self.field.display()


Game()