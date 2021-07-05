from animal import Animal, fstr
from random import choice

class Giraffe(Animal):
    feature = [
                'Everyone knows giraffes for their long necks and their spots.  Did you know their spots are as unique as finger-prints?  No two giraffes have the same exact spot pattern.  Also, you can tell roughly hold old a giraffe is by how dark their spots are.  The older they are, the darker they get!!!',
                'Fun fact about giraffes:  They are herbivores, which means they only eat plants.  Because of how tall they are, they tend to eat leaves off of a tree, and they use their looooonngg tongues to strip the leaves off of the branches.  Some giraffes can get up to two whole feet long!!!  You know how when your bratty brother or sister sticks their tongue at you?  Imagine what a giraffe would look like if they did that!',
                'Giraffes live in the savannahs of Africa and can live up to 25 years old in the wild.  They tend to roam in social groups known as towers, typically around 15 members and led by an adult male.'
              ]

    def __init__(self, name):
        super().__init__(name)
        self.species = 'giraffe'
        self.location = 'the giant giraffe house'


    def features_info(self):
        return fstr(self, choice(self.feature))


