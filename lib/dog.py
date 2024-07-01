#!/usr/bin/env python3

class Dog:
    '''Dog in dog.py'''

    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def get_adopted(self, owner_name):
        self.owner = owner_name

    def get_owner(self):
        return self.owner
    
    