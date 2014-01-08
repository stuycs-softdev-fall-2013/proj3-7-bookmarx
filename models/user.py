from model import Model

class User(Model):
  name = "Default Username"
  tags = []
  def __init__(self, username):
    name = username
    super(User, self).__init__()
  def __repr__(self):
    return "<User %d>"%(self.id)
  def load(self):
    pass
  def unload(self):
    pass
