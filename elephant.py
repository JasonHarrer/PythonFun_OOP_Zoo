from animal import Animal, fstr
from random import choice

class Elephant(Animal):
    feature = [
                'Elephants are the largest of all of the land animals on this planet!!  They are absolutely huge!!  And, of course, large animals means large amounts of food, which means large amounts of poop!!  Watch where you step!!',
                'There are two different types of elephants:  African Elephants and Asian Elephants.  You can tell the difference by their ears.  African Elephants have much bigger ears than the Asian Elephants.  I wonder if this means they can hear better.'
                'An elephant trunk is kind of like one of our arms.  It is used for them to pick up food, to drink water or spray it on themselves as a bath, and they even intertwin trunks with another elephant as a means to say hello and welcome!'
              ]

    def __init__(self, name):
        super().__init__(name)
        self.species = 'elephant'
        self.location = 'the Elephant Habitat'


    def features_info(self):
        return fstr(self, choice(self.feature))

