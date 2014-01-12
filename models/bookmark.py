from model import Model
import database

class Bookmark(Model):
  idnum = 0
  link = "Default link"
  tags = []
  title = "Default Bookmark Title"
  def __init__(self, idnumber):
    self.idnum = idnumber
    super(Bookmark, self).__init__()
  def __repr__(self):
    return "<Bookmark %d>"%(self.id)
  def load(self):
    variables = database.getBookmark(self.idnum)
    if variables != 0:
      self.link = variables[1]
      self.tags = variables[2].split(',')
      self.title = variables[3]
    print self.idnum
    print self.link
    print self.tags
    print self.title
  def unload(self):
    variables = [self.idnum,self.link,','.join(str(v) for v in self.tags),self.title]
    print database.setBookmark(variables)
