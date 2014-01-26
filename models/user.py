from model import Model
import database

class User(Model):
  username = None
  user_id = None
  tags = []
  followed_tags = []
  untagged = []
  repeat_username = False
  def __init__(self, user_id):
    self.user_id = user_id
    self.load()
  def load(self):
    data = database.getUser(self.user_id)
    if data:
      self.username = data['username']
      self.tags = data['tags']
      self.followed = data['followed']
      self.untagged = data['untagged']
  def unload(self):
    database.setUser(self)
  def addTag(self, tag):
    tag.creator = self.user_id
    self.tags.append(tag)
  def addBookmark(self, bookmark):
    bookmark.creator = self.user_id
    self.load()
  def setUsername(self, username):
    self.repeat_username = database.findIfRepeat(username)
    if self.repeat_username:
      return False
    else:
      self.username = username
      return True
