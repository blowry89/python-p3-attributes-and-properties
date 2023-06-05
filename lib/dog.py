#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='Fido', breed='Mastiff'): #initializer 
        self.name = name
        self.breed = breed

    def get_name(self): #getter function
        return self._name
    
    def set_name(self, name): #setter function
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name) #property attribute 

    def get_breed(self): #getter function
        return self._breed
    
    def set_breed(self, breed): #setter function
        if breed in APPROVED_BREEDS: #conditional 
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)
