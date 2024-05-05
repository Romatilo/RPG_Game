from attributes import Attribute
from delivered_attributes import Delivered_attribute
from levels import Level
from skills import Skill
from physical_model import Physical_model
from perks import Perk

class Creature(Attribute, Delivered_attribute, Level, Skill, Physical_model, Perk):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = Physical_model.get_weight()
        self.height = height


    def __str__(self):
        return dict()"name" : self.name, "age" : self.age, "weight" : self.height)
