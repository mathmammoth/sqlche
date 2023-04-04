import sqlite3
import first

the_count = first.counter


this_name = f'Name{the_count}'

with sqlite3.connect('db/database.db') as db:

    cursor = db.cursor()
    cursor.execute(''' INSERT INTO coconut (id, name) VALUES(:the_count, :this_name)  ''', (the_count, this_name))
    db.commit()
