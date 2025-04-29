# class examples
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        '''Simulate a dog siiting'''
        print(f'{self.name} is now sitting')
    
    def roll_over(self):
        '''Simulate a dog rolling over'''
        print(f'{self.name} just rolled over')


class Resturant:
    def __int__(self, resturant_name, cuisine_type):
        '''Initalize the attributes that describes a resturant'''
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
    
    def describe_resturant(self):
        '''print the info about the resturant'''
        print('{0} is a nice {1} restaurant in downtown'.format(self.resturant_name, self.cuisine_type))

    def open_restaurant(self):
        print('The {0} is now open for business!'.format(self.resturant_name))

# AlienCat class
class Aleincat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def go_invisible(self):
        print(f'{self.name} the alien cat just became invisible!')

    def world_destruction(self):
        print(f'The world is at mercy, {self.name} the {self.color} cat is going to blow up earth!')

# Create one (or more) alien cats using the AlienCat class
my_aliencat = Aleincat("Mikey", "purple")
the_aliencat = Aleincat('JOE', 'SUPER HOT RED')
your_aliencat = Aleincat("Charlie", "cyan")

# my_aliencat.go_invisible()
# your_aliencat.go_invisible()
the_aliencat.world_destruction()
print(my_aliencat.color)
print(your_aliencat.color)
