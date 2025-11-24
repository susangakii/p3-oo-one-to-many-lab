class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner")
        self.owner = owner

        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("add_pet expects a Pet instance")

        pet.owner = self

    def get_sorted_pets(self):
        pets_list = self.pets()

        for pet in pets_list:
            if not isinstance(pet, Pet):
                raise Exception("Found a non-Pet instance in owner's pets list")

        return sorted(pets_list, key=lambda pet: pet.name)