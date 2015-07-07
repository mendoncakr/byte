class Animal:
  def __init__(self, sex, age, height, species):
    self.sex = sex
    self.age = age
    self.height = height
    self.species = species

  def speak(self):
    return "Hello, I am a(n) {}".format(self.species)

class Dog(Animal):
  def __init__(self, sex, age, height, species, breed):
    super().__init__(sex, age, height, species)
    self.breed = breed

  def speak(self):
    return "WOOF"

class Cat(Animal):
  def __init__(self, sex, age, height, species, breed, color):
    super().__init__(sex, age, height, species)
    self.breed = breed
    self.color = color

  def speak(self):
    return "MEOW BETCH"

  def my_color(self):
    return "I'm {}".format(self.color)

animal = Animal('Female', 21, '20cm', 'animal')
print(animal.speak())

dog = Dog('Male', 18, '1cm','C. lupus', 'Husky')
print(dog.speak())

cat = Cat('Female', 1000, '0.5cm','F. catus', 'Siamese', 'Grey')
print(cat.speak())
print(cat.my_color())


