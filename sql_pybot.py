import sqlite3
import random

# Define responses related to the GLiCID supercomputer
responses_glicid = {
    "what is GLiCID?": ["GLiCID is a supercomputing center in Nantes used for high-performance computing (HPC) tasks in various scientific and research fields."],
    "where is GLiCID located?": ["GLiCID is located in Nantes."],
    "how can I access GLiCID?": ["To access GLiCID, you'll need to set up SSH access. You can find instructions on setting up SSH access at https://doc.glicid.fr/GLiCID-PUBLIC/latest/."],
    "where can I find documentation for GLiCID?": ["You can find documentation and user guides for GLiCID on the official website or in the documentation section of the GLiCID supercomputer."],
    "what is Slurm?": ["Slurm is a Workload Management System (WMS) that handles resources on the cluster. It is used for job scheduling, resource allocation, and job management on high-performance computing (HPC) clusters like GLiCID."],
    "what is Module command?": ["The Module command is used to manage software environment modules on GLiCID. It allows users to load, unload, and list available modules for their computing needs."],
    "what is Compiler?": ["A compiler is a program that translates source code written in a high-level programming language into machine code that can be executed by the computer's processor. On GLiCID, various compilers are available for different programming languages."],
    "what is Micromamba?": ["Micromamba is a package manager for the Conda ecosystem. It is used on GLiCID for managing and installing software packages and dependencies in Conda environments."],
    "what is Apptainer?": ["Apptainer is a containerization tool used on GLiCID for packaging and deploying applications with their dependencies. It provides a lightweight and portable way to run applications in isolated environments."],
    "what is Podman?": ["Podman is a container management tool similar to Docker. It is used on GLiCID for managing containers and container images, allowing users to run, build, and manage containerized applications."],
    "what is Guix?": ["Guix is a package manager and functional package management tool used on GLiCID. It provides a declarative and reproducible way to manage software packages and environments."],
    "bye": ["Goodbye! Please visit GLiCID documentation for more information."]
}

# SQL syntax
class SQLSyntax:
    CREATE_TABLE = '''
        CREATE TABLE IF NOT EXISTS chatbot (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    '''
    INSERT = 'INSERT INTO chatbot (key, value) VALUES (?, ?)'
    SELECT = 'SELECT value FROM chatbot WHERE key=?'
    DELETE = 'DELETE FROM chatbot WHERE key=?'

# Function to execute SQL commands
def execute_sql(query, values=None):
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    if values:
        cursor.execute(query, values)
    else:
        cursor.execute(query)
    conn.commit()
    result = cursor.fetchall()
    conn.close()
    return result

# Create table if not exists
execute_sql(SQLSyntax.CREATE_TABLE)

# Insert key-value pairs from the chatbot dictionary into the database
for key, value in responses_glicid.items():
    execute_sql(SQLSyntax.INSERT, (key, value[0]))

# Retrieve and print value for a given key
result = execute_sql(SQLSyntax.SELECT, ('what is GLiCID?',))
print("Value for 'what is GLiCID?':", result[0][0] if result else None)

# Delete a key-value pair
execute_sql(SQLSyntax.DELETE, ('what is GLiCID?',))

