from random import choice, randint


class Animal:
    def __init__(self, name):
        self.name = name
        self.age = randint(1, 9)
        self.species = 'animal'
        self.location = 'an enclosure set up to feel like their natural habitat'
        self.health = randint(30, 90)
        self.happiness = randint(30, 90)


    intros = [
               'Here in {self.location}, we have {self.name} the {self.species}.  {self.name} is {self.age} years old.',
               'Looking over on the other side of the tourbus, you will see {self.name} the {self.age}-year old {self.species} living it up in {self.location}!',
               'If you look to your left, you can wave hello to {self.name}, our famous {self.species}.  {self.name} is a {self.age} year old {self.species} that we recently received.',
               'Over to your right in {self.location}, you will find our wonderful {self.species} known as {self.name}.  {self.name} is {self.age} years old and has been a highlight on our tours for some time now.',
               'Oh, would you look at that!!  There is {self.name} in our {self.location}!!  {self.name} is a friendly {self.age} year old {self.species} and has come out to greet you.  Everyone say hello to {self.name}!!'
             ]

    health_good = [
                    '{self.name} is really healthy!  That is because we make sure they are very well taken care of here at our zoo!',
                    '{self.name} recently got a clean bill of health from our zoo veterinarian staff.'
                  ]

    health_poor = [
                    '{self.name} has not been doing the greatest lately.  Our zoo veterinarians have been taking care of them.  Sometimes, it just takes a little more time.',
                    'Looks like someone is feeling a bit under the weather.  Poor {self.name}!!  Get well soon!'
                  ]

    happiness_good = [
                       'Looks like someone is having fun here at the zoo today!!  Look at how happy {self.name} is!!  Look at them play with the toys we have provided for them!',
                       '{self.name} just loves it here at our zoo!!  We know it is not the same as the wild, but they seem to have adapted beautifully.'
                     ]

    happiness_poor = [
                       'Poor {self.name}.  They are missing their home in the wild and their family.  Unfortunately, we are not able to release them back into the wild.  Hopefully {self.name} will acclimate soon.',
                       '{self.name} seems a little down in the dumps today.  Everyone has their bad days.  We hope you feel better tomorrow, {self.name}!!'
                     ]

    def introduction(self):
        return fstr(self, choice(self.intros))


    def health_info(self):
        if self.health > 50:
            return fstr(self, choice(self.health_good))
        else:
            return fstr(self, choice(self.health_poor))


    def happiness_info(self):
        if self.happiness > 50:
            return fstr(self, choice(self.happiness_good))
        else:
            return fstr(self, choice(self.happiness_poor))


    def species(self):
        raise NotImplementedError


    def features_info(self):
        raise NotImplementedError


    def __str__(self): 
        return f'{self.introduction()}\n{self.health_info()}\n{self.happiness_info()}\n{self.features_info()}\n\n\n'


    def display_info(self):
        print(self)


def genderator():
    genders = [ 'Male', 'Female' ]
    return choice(genders)


# Used to refer to f-strings outside of a function.  Adding into animal.py, since all the other modules load animal
# Code from an answer on stack overflow:  https://stackoverflow.com/a/53671539, licensed CC BY-SA 4.0
#   Note, although not an object, using the variable name 'self', since I had already created all the strings using self.
def fstr(self, template):
    return eval(f"f'{template}'\n\n\n")
