class Level():
    def __init__(self, level, experience_points, level_cap):
        self.level = level
        self.experience_points = experience_points        
        self.level_cap = level_cap

        # Getting getters and setters for the level parameters
        def get_level(self):
            return self.level
        def set_level(self, new_level):
            self.level = new_level
        def get_experience_points(self):
            return self.experience_points
        def set_experience_points(self, new_experience_points):
            self.experience_points = new_experience_points
        def level_cap(self):
            return self.level_cap
        def set_level_cap(self, new_level_cap):
            self.level_cap = new_level_cap
