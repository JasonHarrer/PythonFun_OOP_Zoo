from animal import Animal, fstr
from random import choice

class DikDik(Animal):
    feature = [
                'Dik Diks are a very small member of the antelope family, yet still not as small as the West African Royal Antelope.  Diks Diks can grow to about 12 to 16 inches and weigh between 7 and 15 pounds.  Chances are, you know a dog that is bigger than one of these dik diks!!'
                'Dik Diks have a very funny name.  They were named that based on the alarm call a female dik dik makes when they detect a predator.'
                'There are two different ways to tell the difference between a male and a female dik dik.  Male dik diks have small horns, getting up to about 3 inches long, whereas females do not have horns.  Another way to tell is that the female dik diks tend to be larger than the males.'
              ]

    def __init__(self, name):
        super().__init__(name)
        self.species = 'dik dik'
        self.location = 'our mini-savannah habitat'


    def features_info(self):
        return fstr(self, choice(self.feature))

