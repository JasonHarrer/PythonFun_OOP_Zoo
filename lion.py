from animal import Animal, fstr
from random import choice

class Lion(Animal):
    feature = [
                'Male lions have long flowing manes, whereas the female lions do not.  Male lions also tend to have darker fur than the females.',
                'Lions are carnivores.  This means that they are meat-eaters.  These lions love a good antelope steak for dinner!',
                'It is believed that a lion can roar so loud that you could hear it from up to 5 miles away!!!  Are you glad your parents are not that loud, kids?'
              ]

    def __init__(self, name):
        super().__init__(name)
        self.species = 'lion'
        self.location = 'the Lion Den'


    def features_info(self):
        return fstr(self, choice(self.feature))
