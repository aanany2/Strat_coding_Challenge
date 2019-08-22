from garments import Garments

class Hat(Garments):
    def __init__(self):
        super().__init__("1", "hat")

    def rule(self, person):
        if 'shirt' not in person.history:#isinstance implementation
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
        if "socks" not in person.history and "pants" not in person.history:#isinstance implementation
            return False
        else:
            return True # get from super class


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
        result = (all(i in person.history for i in items_to_check ))
        return result

class Person():
    def __init__(self):
        self.history = []

    def take_action(self, key):
        if key == "1":
            garment = Hat()

        elif key == "2":
            garment = Pants()


        elif key == "3":
            garment = Shirt()


        elif key == "4":
            garment = Shoes()


        elif key == "5":
            garment = Socks()


        elif key == "6":
            garment = Leave()

        if garment.rule(self):
            self.history.append(garment.get_value())
        return garment.rule(self), self.history


if __name__ == "__main__":
    input = "5 2 3 4"
    print (input)
    p = Person()
    items = input.split(" ")
    items = filter(None, items)

    for article in items:
        status, history = p.take_action(article)
        if not status:
            history.append('fail')
            break

    items_to_check = ["pants", "shirt", "shoes", "socks"]
    result = (all(i in history for i in items_to_check))
    if result:
        if "leave" not in history:
            history.append("leave")

    print (history)
