class Hero:
    def __init__(self, name, intelligence):
        self.name = name
        self.intelligence = int(intelligence)

    def __str__(self):
        return f"Имя героя: {self.name}\nИнтелект: {self.intelligence}\n"
