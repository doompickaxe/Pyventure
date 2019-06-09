from model.character import Character


class Sailsman(Character):
    pass

    def className(self):
        return "sailsman"

    def __init__(self, name, level):
        super().__init__(name, level, "Aye", "Argh", "the wide wide sea")
