import sqlite3

DB_NAME = "internship.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            college TEXT,
            department TEXT,
            hospital TEXT,
            start_date TEXT,
            end_date TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_intern(name, email, phone, college, department,
               hospital, start_date, end_date, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO interns
        (name, email, phone, college, department, hospital,
         start_date, end_date, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name, email, phone, college, department,
        hospital, start_date, end_date, status
    ))

    conn.commit()
    conn.close()


def get_all_interns():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM interns ORDER BY id DESC")
    data = cursor.fetchall()

    conn.close()
    return data


def update_intern(intern_id, name, email, phone, college,
                  department, hospital, start_date,
                  end_date, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE interns
        SET name = ?,
            email = ?,
            phone = ?,
            college = ?,
            department = ?,
            hospital = ?,
            start_date = ?,
            end_date = ?,
            status = ?
        WHERE id = ?
    """, (
        name, email, phone, college, department,
        hospital, start_date, end_date, status,
        intern_id
    ))

    conn.commit()
    conn.close()


def delete_intern(intern_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM interns WHERE id = ?",
        (intern_id,)
    )

    conn.commit()
    conn.close()