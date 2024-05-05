class Attribute():
    def __init__(self, strength, perception, endurance, charisma, intelligence, agility, luck):
        self.strength = strength
        self.perception = perception        
        self.endurance = endurance
        self.charisma = charisma
        self.intelligence = intelligence
        self.agility = agility
        self.luck = luck

        # getting getters and setters for the attributes
        def get_strength(self):
            return self.strength
        def set_strength(self, new_strength):
            self.strength = new_strength
        def perception(self):
            return self.perception
        def set_perception(self, new_perception):
            self.perception = new_perception
        def get_endurance(self):
            return self.endurance
        def set_endurance(self, new_endurance):
            self.endurance = new_endurance
        def get_charisma(self):
            return self.charisma
        def set_charisma(self, new_charisma):
            self.charisma = new_charisma
        def get_intelligence(self):
            return self.intelligence
        def set_intelligence(self, new_intelligence):
            self.intelligence = new_intelligence
        def get_agility(self):
            return self.agility
        def set_strength(self, new_agility):
            self.agility = new_agility
        def get_luck(self):
            return self.luck
        def set_luck(self, new_luck):
            self.luck = new_luck