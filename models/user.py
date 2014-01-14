from model import Model
import database

class User(Model):
  username = "Default Username"
  token = "No token"
  tags = []
  friends = []
  followed_tags = []
  def __init__(self, name):
    self.username = name
    super(User, self).__init__()
  def __repr__(self):
    return "<User %s>"%(self.token)
  def load(self):
    variables = database.getUser(self.username)
    if variables != 0:
      self.token = variables[1]
      self.tags = variables[2]
      self.friends = variables[3]
      self.followed = variables[4]
  def unload(self):
    variables = [self.username,self.token,",".join(self.tags),",".join(self.friends),",".join(self.followed)]
    database.setUser(variables)
