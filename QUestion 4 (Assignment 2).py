# Class Dog
class Dog:
    def make_sound(self):
        return "Woof! Woof!"


# Class Cat
class Cat:
    def make_sound(self):
        return "Meow! Meow!"


# Function that processes sound
def process_sound(sound_object):
    print(sound_object.make_sound())


# Create objects
dog = Dog()
cat = Cat()

# Pass objects to the same function
process_sound(dog)
process_sound(cat)