class Creature():
    def __init__(self, name, age, weight, height, health_points):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.health_points = health_points

    def __str__(self):
        return dict{"name" : self.name, "age" : self.age, "weight" : self.height}
