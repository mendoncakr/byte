function ToDoList(title) {
  this.title = title
  this.list = [];
}

function Task(description) {
  this.description = description
  this.status = false
}

ToDoList.prototype.add = function(task) {
  this.list.push(task)
}

ToDoList.prototype.complete = function(task) {
  for (var todo in this.list) {
    if (this.list[todo].description === task) {
      this.list[todo].status = true
    } else {
      console.log("Not done!")
    }
  }
}

var myFirstList = new ToDoList("First List")

$(document).ready(function(){

  



})