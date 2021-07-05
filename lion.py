from animal import Animal
from random import choice

class Lion(Animal):
    feature = [
                f'Male lions have long flowing manes, whereas the female lions do not.  Male lions also tend to have darker fur than the females.',
                f'Lions are carnivores.  This means that they are meat-eaters.  These lions love a good antelope steak for dinner!',
                f'It is believed that a lion can roar so loud that you could hear it from up to 5 miles away!!!  Aren\'t you glad your parents aren\'t that loud, kids?'
              ]

    def __init__(self, name, age, health_level=80, happiness_level=40):
        super().__init__(name, age, health_level, happiness_level)


    def features_info(self):
        return choice(self.feature)
