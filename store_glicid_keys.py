import sqlite3

# Define keys related to the GLiCID chatbot
glicid_keys = [
    "what is GLiCID?",
    "where is GLiCID located?",
    "how can I access GLiCID?",
    "where can I find documentation for GLiCID?",
    "what is Slurm?",
    "what is Module command?",
    "what is Compiler?",
    "what is Micromamba?",
    "what is Apptainer?",
    "what is Podman?",
    "what is Guix?",
    "bye"
]

# Create SQLite database and table to store keys
def create_database():
    conn = sqlite3.connect('glicid_chatbot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS glicid_keys
                 (id INTEGER PRIMARY KEY, key TEXT)''')
    conn.commit()
    conn.close()

# Insert keys into the database
def insert_keys():
    conn = sqlite3.connect('glicid_chatbot.db')
    c = conn.cursor()
    for key in glicid_keys:
        c.execute('''INSERT INTO glicid_keys (key) VALUES (?)''', (key,))
    conn.commit()
    conn.close()

# Display all keys stored in the database
def display_keys():
    conn = sqlite3.connect('glicid_chatbot.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM glicid_keys''')
    keys = c.fetchall()
    conn.close()
    for key in keys:
        print(key[0], key[1])

if __name__ == "__main__":
    create_database()
    insert_keys()
    print("Keys stored in the database:")
    display_keys()

