from animals import Cat
from animals import Dog
from animals import Duck

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "cat":
            return Cat()
        elif animal_type == "dog":
            return Dog()
        elif animal_type == "duck":
            return Duck()
        else:
            raise ValueError("Invalid animal type")
