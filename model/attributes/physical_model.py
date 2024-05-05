class Physical_model():
    def __init__(
        self, head,
        eyes,
        body,
        right_forelimb,
        left_forelimb,
        left_hind_limb,
        right_hind_limb,
        groin,
        height,
        weight
    ):
        self.head = head
        self.eyes = eyes
        self.body = body
        self.left_forelimb = left_forelimb
        self.right_forelimb = right_forelimb
        self.left_hind_limb = left_hind_limb
        self.right_hindlimb = right_hind_limb
        self.groin = groin
        self.height = height
        self.weight = weight

    # getting getters and setters for the parts of body
    def get_head(self):
        return self.head

    def set_head(self, new_head):
        self.head = new_head

    def get_body(self):
        return self.body

    def set_body(self, new_body):
        self.body = new_body

    def get_left_forelimb(self):
        return self.left_forelimb

    def set_left_forelimb(self, new_left_forelimb):
        self.left_forelimb = new_left_forelimb

    def get_right_forelimb(self):
        return self.right_forelimb

    def set_right_forelimb(self, new_right_forelimb):
        self.right_forelimb = new_right_forelimb

    def get_left_hind_limb(self):
        return self.left_hind_limb

    def set_left_hind_limb(self, new_left_hind_limb):
        self.left_hind_limb = new_left_hind_limb

    def get_right_hind_limb(self):
        return self.right_hind_limb

    def set_right_hind_limb(self, new_right_hind_limb):
        self.right_hind_limb = new_right_hind_limb

    def get_groin(self):
        return self.groin

    def set_groin(self, new_groin):
        self.groin = new_groin

    def get_groin(self):
        return self.groin

    def set_groin(self, new_groin):
        self.groin = new_groin

    def get_groin(self):
        return self.groin

    def set_groin(self, new_groin):
        self.groin = new_groin

    def get_height(self):
        return self.height

    def set_height(self, new_height):
        self.height = new_height

    def get_weight(self):
        return self.weight

    def set_weight(self, new_weight):
        self.weight = new_weight