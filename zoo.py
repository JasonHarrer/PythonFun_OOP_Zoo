#!/usr/bin/env python

import animal
from lion import Lion
from random import choice, randint

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

                        

animal_types = [ Lion ]


class Zoo:
    intros = [ 'Welcome to my zoo!!  Today, we\'re going to take a ride through the zoo to show you all the wonderful animals we have here!  How exciting is that?\n\n\n',
               'Are you all ready for a fantastical safari ride through my zoo?  Well, buckle up and keep your head, arms and legs inside the vehicles at all times.  Here we go!\n\n\n',
               'Thank you for visiting my zoo today.  Here we have a lot of different animals for you to see, and we\'ll tell you a little bit about each of them as we go.  Are you ready?  Great!!\n\n\n'
             ]


    def __init__(self, num_animals):
        self.animals = []
        for a in range(num_animals):
            new_animal = choice(animal_types)
            new_gender = animal.genderator()
            if new_gender == 'Male':
                new_name = choice(male_animal_names)
            else:
                new_name = choice(female_animal_names)
            self.animals.append(new_animal(new_name, randint(1, 9)))


    def __str__(self):
        s = choice(self.intros)       
        for animal in self.animals:
            s += str(animal)
        return s




if __name__ == '__main__':
    my_zoo = Zoo(randint(1,5))
    print(my_zoo)
