from animal import Animal
from random import choice

class Elephant(Animal):
    feature = [
                f'Elephants are the largest of all of the land animals on this planet!!  They\'re absolutely huge!!  And, of course, large animals means large amounts of food, which means large amounts of poop!!  Watch where you step!!',
                f'There are two different types of elephants:  African Elephants and Asian Elephants.  You can tell the difference by their ears.  African Elephants have much bigger ears than the Asian Elephants.  I wonder if this means they can hear better.'
                f'An elephant\'s trunk is kind of like one of our arms.  It is used for them to pick up food, to drink water or spray it on themselves as a bath, and they even intertwin trunks with another elephant as a means to say hello and welcome!'
              ]

    def __init__(self, name, age, health_level=45, happiness_level=80):
        super().__init__(name, age, health_level, happiness_level)
        self.species = 'elephant'
        self.location = 'the Elephant Habitat'


    def features_info(self):
        return choice(self.feature)

