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

def create_animal(animal):
    max_id = ANIMALS[-1]["id"]
    new_id = max_id + 1
    animal['id'] = new_id
    ANIMALS.append(animal)

    return animal

def delete_animal(id):
    animal_index = -1
    taco = 'id'
    for (index, animal) in enumerate(ANIMALS):
        if animal[taco] == id:
            animal_to_remove = animal
    
    if animal_index >= 0:
        ANIMALS.remove(animal_to_remove)

def update_animal(id, updated_animal):
    for index, animal in enumerate(ANIMALS):
        if animal['id'] == id:
            ANIMALS[index] = updated_animal
            break
