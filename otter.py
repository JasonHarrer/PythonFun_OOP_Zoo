from animal import Animal, fstr
from random import choice

class Otter(Animal):
    feature = [
                'There are 13 different types of otters, which are part of the weasel family.  This here is a North American river otter.  River otters are smaller than the sea otters that some may be used to seeing.  River otters can get up to 42 inches long and up to about 30 pounds.  At least a third of their length is their tail, getting up to as big as 20 inches in length!'
                'Otters are active year round, but they tend to be most active at night.  That is when they hunt for food, which can include fish, crustaceans, certain birds, insects, small reptiles and amphibians, in rare occasion, small mammals like rabbits.  No, not like your baby brother.',
                'Many otters in the world are found around North America.  There are many sea otters that live in the waters around Alaska, kept warm by their super-thick fur.  Sea otters can be found a lot more commonly in the warmer waters, closer to the Pacific Northwest, the Gulf Coast, or the East Coast.  River otters tend to be found more by freshwaters, such as inland wetlands, marshes, lakes, rivers, and other similar environments.'
              ]

    def __init__(self, name):
        super().__init__(name)
        self.species = 'otter'
        self.location = 'our Wonderful World of Water Habitat'


    def features_info(self):
        return fstr(self, choice(self.feature))


