# Single inheritance
class Parent:
    def parent_method(self):
        print("This is parent method.")

class Child(Parent):
    def child_method(self):
        print("This is child method.")

# Multiple inheritance
class Dog:
    def sound(self):
        print("Woof!")

class Bird:
    def sound(self):
        print("Chirp!")

class DogBird(Dog, Bird):
    pass

# Multilevel inheritance
class Grandparent:
    def grandparent_method(self):
        print("This is grandparent method.")

class Parent(Grandparent):
    def parent_method(self):
        print("This is parent method.")

class Grandchild(Parent):
    def grandchild_method(self):
        print("This is grandchild method.")

# Single inheritance example
print("Single inheritance:")
child = Child()
child.parent_method()
child.child_method()
print()

# Multiple inheritance example
print("Multiple inheritance:")
dog_bird = DogBird()
dog_bird.sound()
print()

# Multilevel inheritance example
print("Multilevel inheritance:")
grandchild = Grandchild()
grandchild.grandparent_method()
grandchild.parent_method()
grandchild.grandchild_method()
