from model.character import Character


class Rogue(Character):
    pass

    def className(self):
        return "rogue"

    def __init__(self, name, level):
        super().__init__(name, level, "Maybe", "Maybe not", "the underground")
