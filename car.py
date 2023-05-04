
class Car:
    # Class attribute
    num_wheels = 4
   
    def __init__(self, make, model, year):
        # Instance variables
        self.make = make
        self.model = model
        self.year = year
       
    def start(self):
        print("The car has started.")
       
    def stop(self):
        print("The car has stopped.")
       
    def get_make(self):
        return self.make
   
    def get_model(self):
        return self.model
   
    def get_year(self):
        return self.year
