class Animal():
    def __init__(self, id, name, breed, status, location_id = 1):
        self.id = id
        self.name = name
        self.breed = breed
        self.status = status
        self.location_id = location_id


animal1 = Animal(1, 'Jack', 'husky', 'napping')
print(animal1.name)
print(f"Jack's location {animal1.location_id}")
animal2 = Animal(2, 'Eleanor', 'Mix', 'napping', 2)
print(animal2.name)
print(f"{animal2.name}'s location {animal2.location_id}")

# animal3 = Animal()
# animal3.name = 'Jack'
# print(animal3.name)

# animal4 = Animal()
# print(animal4.name)
