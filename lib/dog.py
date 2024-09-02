#!/usr/bin/env python3


class Dog:

    APPROVED_BREEDS = ["Mastiff","Chihuahua","Corgi","Shar Pei","Beagle","French Bulldog","Pug","Pointer"]

    def __init__(self,name="niko",breed="Chihuahua"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self,name):
        if isinstance(name,str) and  1<=len(name)<=25:
            self._name = name
        
        else:
             print("Name must be string between 1 and 25 characters.")




    @property
    def breed(self):
        return self._breed   

    @breed.setter
    def breed(self,breed):
        if breed in Dog.APPROVED_BREEDS:
            self._breed = breed

        else:
            print("Breed must be in list of approved breeds.")

