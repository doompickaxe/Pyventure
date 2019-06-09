from model.character import Character


class Farmer(Character):
    pass

    def className(self):
        return "farmer"

    def __init__(self, name, level):
        super().__init__(name, level, "Yes", "No", "the shire")
