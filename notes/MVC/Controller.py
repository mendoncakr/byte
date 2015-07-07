from Model import Model
from View import View

class Controller(object):
  def __init__(self):
    self.model = Model()
    self.view = View()

  def run(self):
    name = self.view.welcome()
    if name == 'Ken':
      print(self.model.say_hello(name))
    else:
      print(self.model.say_bye())





Controller().run()