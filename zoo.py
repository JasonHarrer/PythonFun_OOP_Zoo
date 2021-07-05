#!/usr/bin/env python

from random import choice, randint

from animal import Animal, fstr, genderator

from dikdik import DikDik
from elephant import Elephant
from giraffe import Giraffe
from lion import Lion
from otter import Otter

male_animal_names =   [ "Alfred",  "Bobby",   "Chip",    "Don",    "Eddie", 
                        "Freddie", "Greg",    "Harry",   "Ira",    "Jimmy",
                        "Kevin",   "Leo",     "Moe",     "Noah",   "Obie",
                        "Pete",    "Quincy",  "Rich",    "Steve",  "Tommy",
                        "Urie",    "Vic",     "Wally",   "Xavi",   "Yogi",
                        "Zeus" ]

female_animal_names = [ "Alice",   "Brianne", "Carla",   "Dianne", "Esme",
                        "Flo",     "Gladys",  "Haley",   "Ivy",    "Jenny",
                        "Kim",     "Laura",   "Maisie",  "Nicky",  "Olive",
                        "Phoebe",  "Queenie", "Rue",     "Sari",   "Tessa",
                        "Uliana",  "Vana",    "Whitney", "Xena",   "Yasmine",
                        "Zhen" ]

                        

animal_types = [ DikDik, Elephant, Giraffe, Lion, Otter ]


class Zoo:
    intros = [
               "Welcome to {self.name}!!  Today, we are going to take a ride through the zoo to show you all the wonderful animals we have here!  How exciting is that?",
               "Are you all ready for a fantastical safari ride through {self.name}?  Well, buckle up and keep your head, arms and legs inside the vehicles at all times.  Here we go!",
               "Thank you for visiting {self.name} today.  Here we have a lot of different animals for you to see, and we will tell you a little bit about each of them as we go.  Are you ready?  Great!!"
             ]


    def __init__(self, zoo_name, num_animals):
        self.name = zoo_name
        self.animals = []
        for a in range(num_animals):
            new_animal = choice(animal_types)
            animal_types.remove(new_animal)
            new_gender = genderator()
            if new_gender == 'Male':
                new_name = choice(male_animal_names)
                male_animal_names.remove(new_name)
            else:
                new_name = choice(female_animal_names)
                female_animal_names.remove(new_name)
            self.animals.append(new_animal(new_name))


    def __str__(self):
        s = fstr(self, choice(self.intros))
        s += '\n\n\n'
        for animal in self.animals:
            s += str(animal)
        return s




if __name__ == '__main__':
    my_zoo = Zoo('The International Zoo Of Awesomeness', randint(3,5))
    print(my_zoo)
