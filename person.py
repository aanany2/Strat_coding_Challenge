from src.garments import Garments, Hat,Pants,Shirt,Shoes,Socks,Leave

class Person():
    #TODO: Put this in config file
    options = {'1': Hat,
               '2': Pants,
               '3': Shirt,
               '4': Shoes,
               '5': Socks,
               '6': Leave
               }

    def __init__(self):
        self.history = []

    def take_action(self, key):

        garment = self.options[key]()

        if garment.rule(self):
            self.history.append(garment.get_value())
        return garment.rule(self), self.history
