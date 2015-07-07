import sqlite3
db = sqlite3.connect('school.db')
c = db.cursor()

class Student(object):
  def __init__(self, id, name, age, gender):
     self.id = id
     self.name  = name 
     self.age  = age 
     self.gender = gender

class Klass(object):
  def __init__(self, title):
    self.title = title

class School(object):
  def __init__(self, name):
    self.name = name

  def add_new_student(self, student):
    c.execute("INSERT INTO students VALUES(?,?,?,?)", [student.id, student.name, student.age, student.gender])
    db.commit()

  def find_student_by_name(self, student):
    c.execute("SELECT * FROM students WHERE name=?", (student.name,))
    user = c.fetchall()
    return user


bob = Student(1, 'Bob Smalls', 45, 'male')
byte = School('Byte Academy')
byte.add_new_student(bob)
byte.find_student_by_name(bob)