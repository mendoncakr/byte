import sqlite3
from faker import Faker

db = sqlite3.connect('school.db')
c = db.cursor()

c.execute("DROP TABLE IF EXISTS 'students'")
c.execute("DROP TABLE IF EXISTS 'klass'")

def create_tables():
  c.execute('''
    CREATE TABLE students(
      id INTEGER DEFAULT NULL PRIMARY KEY AUTOINCREMENT,
      name VARCHAR DEFAULT NULL,
      age VARCHAR  DEFAULT NULL,
      gender VARCHAR DEFAULT NULL
      );
  ''')

  c.execute('''
    CREATE TABLE klass(
      id INTEGER DEFAULT NULL PRIMARY KEY AUTOINCREMENT,
      title VARCHAR DEFAULT NULL,
      student_id  INTEGER DEFAULT NULL,
      FOREIGN KEY(student_id) REFERENCES students(id)
      );
  ''')
  db.commit()

create_tables()
# seed_users()

