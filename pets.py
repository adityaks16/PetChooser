# Aditya Kunapareddy
# Purpose: This file defines the Pets class for the Pet Chooser program
# It includes:
# - Constructor to create Pet objects
# - Getter methods for pet attributes
# - String representation of a Pet

class Pets:
    def __init__(self, name, age, owner, animal_type):
        # Initialize a new Pet object
        self._name = name
        self._age = age
        self._owner = owner
        self._animal_type = animal_type

    def get_name(self):
        # Return the pet's name
        return self._name

    def get_age(self):
        # Return the pet's age
        return self._age

    def get_owner(self):
        # Return the pet's owner
        return self._owner

    def get_animal_type(self):
        # Return the pet's animal type
        return self._animal_type

    def __str__(self):
        # Return a string representation of the pet
        return f"{self._name}, the {self._animal_type}. {self._name} is {self._age} years old. {self._name}'s owner is {self._owner}."