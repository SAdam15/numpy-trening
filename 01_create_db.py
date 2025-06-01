import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Połączono z bazą danych:", db_file)
    except Error as e:
        print("Błąd połączenia:", e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Tabela utworzona poprawnie.")
    except Error as e:
        print("Błąd tworzenia tabeli:", e)

def insert_project(conn, project):
    sql = '''INSERT INTO projects(name, begin_date, end_date)
             VALUES(?, ?, ?)'''
    try:
        cur = conn.cursor()
        cur.execute(sql, project)
        conn.commit()
        print("Projekt dodany:", project)
        return cur.lastrowid
    except Error as e:
        print("Błąd dodawania projektu:", e)
        return None

def insert_task(conn, task):
    sql = '''INSERT INTO tasks(project_id, name, description, status, start_date, end_date)
             VALUES(?, ?, ?, ?, ?, ?)'''
    try:
        cur = conn.cursor()
        cur.execute(sql, task)
        conn.commit()
        print("Zadanie dodane:", task)
        return cur.lastrowid
    except Error as e:
        print("Błąd dodawania zadania:", e)
        return None

def main():
    database = "database.db"

    sql_create_projects_table = """
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        begin_date TEXT,
        end_date TEXT
    );
    """

    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        description TEXT,
        status TEXT NOT NULL,
        start_date TEXT,
        end_date TEXT,
        FOREIGN KEY (project_id) REFERENCES projects (id)
    );
    """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_tasks_table)

        new_project = ("Projekt Python", "2025-05-13", "2025-06-30")
        project_id = insert_project(conn, new_project)

        if project_id:
            task = (
                project_id,
                "Stworzenie bazy danych",
                "Utworzenie struktury SQLite",
                "w toku",
                "2025-05-13",
                "2025-05-14"
            )
            insert_task(conn, task)

        conn.close()
    else:
        print("Nie udało się połączyć z bazą danych.")

if __name__ == "__main__":
    main()
    