from model import Model
import database

class Bookmark(Model):
  idnum = 0
  link = "Default link"
  tags = []
  name = "Default Bookmark Title"
  def __init__(self, idnumber=-1):
    self.idnum = idnumber
    super(Bookmark, self).__init__()
  def __repr__(self):
    return "<Bookmark %d>"%(self.idnum)
  def load(self):
    variables = database.getBookmark(self.idnum)
    if variables != 0:
      self.link = variables[1]
      self.name = variables[2]
      self.tags = variables[3]
  def unload(self):
    database.setBookmark(self.idnum,self.link,self.title,self.tags)
