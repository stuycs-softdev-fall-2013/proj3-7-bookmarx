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
    return "<User %d>"%(self.id)
  def load(self):
    variables = database.getUser(self.name)
    if variables != 0:
      self.token = variables[1]
      self.tags = variables[2].split(',')
      self.friends = variables[3].split(',')
      self.followed = variables[4].split(',')
  def unload(self):
    variables = [self.name,self.token,",".join(self.tags),",".join(self.friends),",".join(self.followed)]
    database.setUser(variables)
