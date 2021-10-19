import json
import sqlite3
from models import Animal

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
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        from animal as a
        """)

        dataset = db_cursor.fetchall()
        animals = []

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['status'], row['location_id'])
            animals.append(animal.__dict__)
    return json.dumps(animals)

def get_single_animal(id):
    with sqlite3.connect('./kennel.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        select *
        from animal
        where id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        animal = Animal(data['id'], data['name'], data['status'], data['location_id'])
        return json.dumps(animal.__dict__)

def create_animal(animal):
    max_id = ANIMALS[-1]["id"]
    new_id = max_id + 1
    animal['id'] = new_id
    ANIMALS.append(animal)

    return animal

def delete_animal(id):
    with sqlite3.connect('./kennel.db') as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
            DELETE FROM animal
            where id = ?
        """, (id, ))
    # conn = sqlite3.connect('./kennel.db')
    # # execute sql
    # conn.close()
def update_animal(id, updated_animal):
    for index, animal in enumerate(ANIMALS):
        if animal['id'] == id:
            ANIMALS[index] = updated_animal
            break
