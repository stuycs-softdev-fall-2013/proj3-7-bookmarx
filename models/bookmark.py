from model import Model
import database

class Bookmark(Model):
  idnum = -1
  tags = []
  link = "Default link"
  name = "Default Bookmark Title"
  def __init__(self, link, title):
    self.link = link
    self.title = title
    self.load()
  def __repr__(self):
    return "<Bookmark %d>"%(self.idnum)
  def load(self):
    variables = database.getBookmark(self)
    if variables:
      self.link = variables[1]
      self.name = variables[2]
      self.tags = variables[3]
  def unload(self):
    database.setBookmark(self)
