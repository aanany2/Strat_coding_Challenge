class Garments():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def rule(self, person):
        return True

    def get_value(self):
        return self.value

