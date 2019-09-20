class Garments():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def rule(self, person):
        return True

    def get_value(self):
        return self.value


class Hat(Garments):
    def __init__(self):
        super().__init__("1", "hat")

    def rule(self, person):
        '''

        :param person:
        :return:
        '''
        if 'shirt' not in person.history:  # isinstance implementation
            return False
        else:
            return True


class Pants(Garments):
    def __init__(self):
        super().__init__("2", "pants")

    def rule(self, person):
        return True


class Shirt(Garments):
    def __init__(self):
        super().__init__("3", "shirt")

    def rule(self, person):
        return True


class Shoes(Garments):
    def __init__(self):
        super().__init__("4", "shoes")

    def rule(self, person):
        if "socks" not in person.history and "pants" not in person.history:  # isinstance implementation
            return False
        else:
            return True  # get from super class


class Socks(Garments):
    def __init__(self):
        super().__init__("5", "socks")

    def rule(self, person):
        return True


class Leave(Garments):
    def __init__(self):
        super().__init__("6", "leave")

    def rule(self, person):
        items_to_check = ["pants", "shirt", "shoes", "socks"]
        result = (all(i in person.history for i in items_to_check))
        return result