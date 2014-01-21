from model import Model
import database

class User(Model):
  username = None
  user_id = None
  tags = []
  friends = []#This will only contain the usernames of friends
  followed_tags = []
  def __init__(self, token):
    self.token = token
    self.load()
  def load(self):
    data = database.getUser(self.token)
    if data:
      self.name = data['username']
      self.tags = data['tags']
      self.friends = data['friends']
      self.followed = data['followed']
  def unload(self):
    database.setUser(self)
  def addTag(self, tag):
    tag.creator = self.user_id
    self.tags.append(tag.idnum, tag.name, tag.description, tag.color, tag.creator, tag.privacy)
