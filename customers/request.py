import sqlite3
import json
from models.customer import Customer


def get_customers_by_email(email):
    with sqlite3.connect('./kennel.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select *
        from Customer 
        where email like ?
        """, (f'%{email}%', ))

        customers = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'])
            customers.append(customer.__dict__)

        return json.dumps(customers)
