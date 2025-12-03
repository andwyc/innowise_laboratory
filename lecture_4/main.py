import sqlite3

def main():
    # Connect to (or create) the SQLite database file and create a cursor
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # Read and execute the SQL script
    cursor.execute("PRAGMA foreign_keys = ON;")
    with open("scripts.sql", "r", encoding="utf-8") as file:
        sql_script = file.read()
    cursor.executescript(sql_script)

    # Save changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()