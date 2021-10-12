ANIMALS = [
    {
        "id": 1,
        "name": "Snickers"
    },
    {
        "id": 2,
        "name": "Gypsy"
    }
]
# const animals = []

def get_all_animals():
    return ANIMALS

def get_single_animal(id):
    # let requestedAnimal;
    requested_animal = None

    for animal in ANIMALS:
        if animal['id'] == id:
            requested_animal = animal

    return requested_animal
