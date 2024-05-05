from attributes import Attribute
from levels import Level

class Delivered_attribute():
    def __init__(
        self, action_points,
        armor_class,
        carry_weight,
        critical_chance,
        damage_resistance,
        damage_treshold,
        healin_rate,
        hit_points,
        melee_damage,
        perk_rate,
        poison_resistance,
        radiation_resistance,
        sequence,
        skill_rate
    ):
        self.action_points = action_points
        self.armor_class = armor_class
        self.carry_weight = carry_weight
        self.critical_chance = critical_chance
        self.damage_resistance = damage_resistance
        self.damage_treshold = damage_treshold
        self.healin_rate = healin_rate
        self.hit_points = hit_points
        self.melee_damage = melee_damage
        self.perk_rate = perk_rate
        self.poison_resistance = poison_resistance
        self.radiation_resistance = radiation_resistance
        self.sequence = sequence
        self.skill_rate = skill_rate

        # getting getters and setters for the delivered_attributes values
        def get_action_points(self):
            return self.action_points

        def set_action_points(self, new_action_points):
            self.action_points = new_action_points

        def get_armor_class(self):
            return self.armor_class

        def set_armor_class(self, new_armor_class):
            self.armor_class = new_armor_class

        def get_carry_weight(self):
            return self.carry_weight

        def set_carry_weight(self, new_carry_weight):
            self.carry_weight = new_carry_weight

        def get_critical_chance(self):
            return self.critical_chance

        def set_critical_chance(self, new_critical_chance):
            self.critical_chance = new_critical_chance

        def get_damage_resistance(self):
            return self.damage_resistance

        def set_damage_resistance(self, new_damage_resistance):
            self.damage_resistance = new_damage_resistance

        def get_damage_tresholde(self):
            return self.damage_treshold

        def set_damage_treshold(self, new_damage_treshold):
            self.damage_treshold = new_damage_treshold

        def get_healin_rate(self):
            return self.healin_rate

        def set_healin_rate(self, new_healin_rate):
            self.healin_rate = new_healin_rate

        def get_hit_points(self):
            return self.hit_points

        def set_hit_points(self, new_hit_points):
            self.hit_points = new_hit_points

        def get_melee_damage(self):
            return self.melee_damage

        def set_melee_damage(self, new_melee_damage):
            self.melee_damage = new_melee_damage

        def get_perk_rate(self):
            return self.perk_rate

        def set_perk_rate(self, new_perk_rate):
            self.perk_rate = new_perk_rate

        def get_poison_resistance(self):
            return self.poison_resistance

        def set_poison_resistance(self, new_poison_resistance):
            self.poison_resistance = new_poison_resistance

        def get_radiation_resistance(self):
            return self.radiation_resistance

        def set_radiation_resistance(self, new_radiation_resistance):
            self.radiation_resistance = new_radiation_resistance

        def get_sequence(self):
            return self.sequence

        def set_sequence(self, new_sequence):
            self.sequence = new_sequence

        def skill_rate(self):
            return self.skill_rate

        def set_skill_rate(self, new_skill_rate):
            self.skill_rate = new_skill_rate

        # set formulas for the delivered attributes depends on attributes


        
        # Action points (AP)
        # 5 + AG / 2
        def calc_action_points(self, agility):
            self.action_points = 5 + agility//2
            return action_points

        # Armor class(AC)
        # Armor Class = Agility



        # Hit points
        # 15 + 2 * EN + ST
        # Every time you gain a level this increases by 2 + EN / 2
        def calc_hit_points(self, strength, endurance, level):
            strength = Attributes.get_strength()
            endurance = Attributes.get_endurance()
            level = Level.get_level()
            self.hit_points = 15 + 2*Attributes.endurance + strength + (2 + endurance)*level//2
            return hit_points


Attribute.set_strength(1)
print (Attribute.get_strength())

