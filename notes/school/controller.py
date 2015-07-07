from views import SchoolView

class SchoolController:
  def __init__(self):
    self.view = SchoolView()

  def home_screen(self):
    self.view.welcome()




SchoolController().home_screen()