# Python classes

class Dog(object):
  #  Our __init__ method below instaniates a new Dog object. It is absolutely necessary in order to create new instances of this object. By passing arguments to our init function, we can create instance variable for our object. Instance variables are variables that can be used only WITHIN the scope of the object. By doing so, we are creating attributes for our dog that we can manipulate in various ways within our code.
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

  # In order to create "behaviors" for our Dog object, we create instance methods. These methods allows us to model behaviors of dogs. 
  def bark(self):
    print "BARK BARK"




# Let's instaniate a new Dog object
dogOne = Dog("Doge", "Pitbull", 100)
print dogOne.name # ==> "Doge"
print dogOne.breed # ==> "Pitbull"
print dogOne.age # ==> 100
