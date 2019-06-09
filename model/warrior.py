from model.character import Character


class Warrior(Character):
    pass

    def className(self):
        return "warrior"

    def __init__(self, name, level):
        super().__init__(name, level, "Yes, Sir", "No, Sir", "the first legion")
