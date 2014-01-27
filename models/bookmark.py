from model import Model
import database

class Bookmark(Model):
  idnum = -1
  tags = []
  link = "Default link"
  title = "Default Bookmark Title"
  creator = "Default creator"
  def __init__(self, title=None, link=None, idnum=None):
    if idnum:
      self.idnum = idnum
    else:
      self.title = title
      self.link = link
    self.load()
  def __repr__(self):
    return "<Bookmark %d>"%(self.idnum)
  def load(self):
    variables = database.getBookmark(self)
    if len(variables) == 1:
      self.idnum = variables[0]
    else:
      self.link = variables[1]
      self.title = variables[2]
      self.creator = variables[3]
      self.tags = variables[4]
  def unload(self):
    database.setBookmark(self)
  def addTag(self, tag):
    self.tags.append(tag)
    tag.bookmarks.append(self)
