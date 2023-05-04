
class Fruit:
    # Class attribute
    is_healthy = True
   
    def __init__(self, name, color, price):
        # Instance variables
        self.name = name
        self.color = color
        self.price = price
       
    def is_expensive(self):
        if self.price > 5:
            return True
        else:
            return False
       
    def get_name(self):
        return self.name
   
    def get_color(self):
        return self.color
   
    def get_price(self):
        return self.price