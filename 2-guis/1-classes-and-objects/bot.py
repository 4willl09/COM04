class Bot:
    def __init__ (self, name, age , energy , shield_level ):
    self.name = name 
    self.age = age
    self.energy = energy 
    self.shield_level = shield_level

    def display_name (self):
        print ("The name is {}".format(self.name) )
    def display_age (self):
        print ("Age of {} is {}".format(self.name, self.age))
    def display_energy (self):
        print ("current energy levels at {}".format (self.energy) )
    def display_shield (self):
        print ("shield level at {}".format (self.shield_level))
    def display_summary (self):
        print ("system summary")
    
    bot = Bot ("Bot",2001,68,70)