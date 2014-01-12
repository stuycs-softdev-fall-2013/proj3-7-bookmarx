from model import Model
import database

class User(Model):
  name = "Default Username"
  token = ""
  tags = []
  friends = []
  followed = []
  def __init__(self, username):
    self.name = username
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
      print self.token
      print self.tags
      print self.friends
      print self.followed
  def unload(self):
    variables = [self.name,self.token,",".join(self.tags),",".join(self.friends),",".join(self.followed)]
    database.setUser(variables)
