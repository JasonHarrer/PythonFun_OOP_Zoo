from random import choice


class Animal:
    def __init__(self, name, age, health_level=75, happiness_level=50):
        self.name = name
        self.age = age
        self.location = ' an enclosure set up to feel like their natural habitat'
        self.health = health_level
        self.happiness = happiness_level


    def introduction(self):
        intros = [
                   f'Here in {self.location}, we have {self.name}.',
                   f'Looking over on the other side of the tourbus, you\'ll see {self.name} living it up in {self.location}!'
                 ]
        return choice(intros)


    def health_info(self):
        health_good = [
                         f'{self.name} is really healthy!  That\'s because we make sure they are very well taken care of here at our zoo!',
                         f'{self.name} recently got a clean bill of health from our zoo\'s veterinarian staff.'
                      ]

        health_poor = [ f'{self.name} hasn\'t been doing the greatest lately.  Our zoo veterinarians have been taking care of them.  Sometimes, it just takes a little more time.',
                        f'Looks like someone\'s feeling a bit under the weather.  Poor {self.name}!!  Get well soon!'
                      ]

        if self.health > 50:
            return choice(health_good)
        else:
            return choice(health_poor)


    def happiness_info(self):
        happiness_good = [
                           f'Looks like someone is having fun here at the zoo today!!  Look at how happy {self.name} is!!  Look at them play with the toys we\'ve provided for them!',
                           f'{self.name} just loves it here at our zoo!!  We know it\'s not the same as the wild, but they seem to have adapted beautifully.'
                         ]

        happiness_poor = [
                           f'Poor {self.name}.  They\'re missing their home in the wild and their family.  Unfortunately, we\'re not able to release them back into the wild.  Hopefully {self.name} will acclimate soon.',
                           f'{self.name} seems a little down in the dumps today.  Everyone has their bad days.  We hope you feel better tomorrow, {self.name}!!'
                         ]
        if self.happiness > 50:
            return choice(happiness_good)
        else:
            return choice(happiness_poor)


    def features_info(self):
        raise NotImplementedError


    def __str__(self): 
        return f'{self.introduction()}\n{self.health_info()}\n{self.happiness_info()}\n{self.features_info()}\n\n'



def genderator():
    genders = [ 'Male', 'Female' ]
    return choice(genders)
