//  The Function constructor creates a new Function object. In JavaScript every function is actually a Function object.

function Dog(name, breed, age) {
  this.name = name;
  this.breed = breed;
  this.age = age;
}

// Instaniate a new instance of our dog function object
var dogOne = new Dog("Doge", "Pitbull", 100)

// To access the properties of our Dog object we can:
dogOne.name // ==> "Doge"
dogOne.breed // ==> "Pitb"
dogOne.age // ==> 100

// Turns out we need to add new functionality to our existing Dog object. Apparently, these guys can bark() and poop(). There are two ways we can create functions/methods for our Dog object.

// First way: Add directly to the constructor
function Dog(name, breed, age) {
  this.name = name;
  this.breed = breed;
  this.age = age;
  this.bark = function() {
    console.log("BARK BARK")
  }
}
var dogOne = new Dog("Doge", "Pitbull", 100)
dogOne.bark()


// Second way: Add to the prototype of our Dog object
Dog.prototype.bark = function() {
  console.log("BARK BARK")
}
var dogOne = new Dog("Doge", "Pitbull", 100)
dogOne.bark()




