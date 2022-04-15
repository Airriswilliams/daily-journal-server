import sqlite3
import json
from models import Entry, Mood


ENTRIES = [
   {
      "concept": "Javascript",
      "entry": "I learned about loops today. They can be a lot of fun.\nI learned about loops today. They can be a lot of fun.\nI learned about loops today. They can be a lot of fun.",
      "moodId": 1,
      "date": "Wed Sep 15 2021 10:10:47 ",
      "id": 1
    },
    {
      "concept": "Python",
      "entry": "Python is named after the Monty Python comedy group from the UK. I'm sad because I thought it was named after the snake",
      "moodId": 4,
      "date": "Wed Sep 15 2021 10:11:33 ",
      "id": 2
    },
    {
      "concept": "Python",
      "entry": "Why did it take so long for python to have a switch statement? It's much cleaner than if/elif blocks",
      "moodId": 3,
      "date": "Wed Sep 15 2021 10:13:11 ",
      "id": 3
    },
    {
      "concept": "Javascript",
      "entry": "Dealing with Date is terrible. Why do you have to add an entire package just to format a date. It makes no sense.",
      "moodId": 3,
      "date": "Wed Sep 15 2021 10:14:05 ",
      "id": 4
    } 
]


def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.mood_id,
            e.concept,
            e.entry,
            e.date,
            m.label mood_label
        FROM Entry As e
        JOIN Moods As m
        ON m.id = e.mood_id
        """)
           

        # Initialize an empty list to hold all entry representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Entry class above.
            entry = Entry(row['id'], row['mood_id'], row['concept'],
                            row['entry'], row['date'])
            
            mood = Mood(row['id'], row['mood_label'])
            
            entry.mood = mood.__dict__
            
            entries.append(entry.__dict__)
            
    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)
                            


# Function with a single parameter
def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.mood_id,
            e.concept,
            e.entry,
            e.date
        FROM Entry e
        WHERE e.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an entry instance from the current row
        entry = Entry(data['id'], data['mood_id'], data['concept'],
                            data['entry'], data['date'])
                            

        return json.dumps(entry.__dict__)


def delete_entry(id):
     with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Entry
        WHERE id = ?
        """, (id, ))
        
def create_journal_entry(new_entry):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Entry
            ( mood_id, concept, entry, date)
        VALUES
            ( ?, ?, ?, ?);
        """, (new_entry['moodId'], new_entry['concept'],
              new_entry['entry'], new_entry['date'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the entry dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_entry['id'] = id


    return json.dumps(new_entry)


def update_entry(id, new_entry):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Entry
            SET
                mood_id = ?,
                concept = ?,
                entry = ?,
                date = ?
        WHERE id = ?
        """, (new_entry['mood_id'], new_entry['concept'],
              new_entry['entry'], new_entry['date'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True