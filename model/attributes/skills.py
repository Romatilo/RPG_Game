# more skills: coock,

class Skill():
    def __init__(self, guns, unarmed, melee_weapons, lockpick, sneak, steal, medicine, speach):
        self.guns = guns
        self.unarmed = unarmed
        self.melee_weapons = melee_weapons
        self.lockpick = lockpick
        self.sneak = sneak
        self.steal = steal
        self.medicine = medicine
        self.speach = speach

        # getting getters and setters for the skills
        def get_guns(self):
            return self.guns

        def set_guns(self, new_guns):
            self.guns = new_guns

        def get_unarmed(self):
            return self.unarmed

        def set_unarmed(self, new_unarmed):
            self.unarmed = new_unarmed

        def get_melee_weapons(self):
            return self.melee_weapons

        def set_melee_weapons(self, new_melee_weapons):
            self.melee_weapons = new_melee_weapons

        def get_lockpick(self):
            return self.lockpick

        def set_lockpick(self, new_lockpick):
            self.lockpick = new_lockpick

        def get_sneak(self):
            return self.sneak

        def set_sneak(self, new_sneak):
            self.sneak = new_sneak

        def get_steal(self):
            return self.steal

        def set_steal(self, new_steal):
            self.steal = new_steal

        def get_medicine(self):
            return self.medicine

        def set_medicine(self, new_medicine):
            self.medicine = new_medicine

        def get_speach(self):
            return self.speach

        def set_speach(self, new_speach):
            self.speach = new_speach

        # set formulas for the skills depends on attributes and delivered attributes 
