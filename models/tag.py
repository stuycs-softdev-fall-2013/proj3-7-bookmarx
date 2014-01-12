from model import Model
import database

class Tag(Model):
  idnum = 0
  name = "Default Tag Name"
  description = "Default Tag Description"
  color = [0, 0, 0] # Store color as RGB list, I guess. Probably FIXME
  creator = None # User who created the tag
  bookmarks = [] # Bookmarks with this tag
  privacy = "private" # We probably want something more like an enum here, FIXME
  def __init__(self, idnumber):
    self.idnum = idnumber
    super(Tag, self).__init__()
  def __repr__(self):
    return "<Tag %d>"%(self.id)
  def load(self):
    variables = database.getTag(self.idnum)
    if variables != 0:
      self.name = variables[1]
      self.description = variables[2]
      self.color = variables[3].split(',')
      self.creator = variables[4]
      self.bookmarks = variables[5].split(',')
      self.privacy = variables[6]
  def unload(self):
    variables = [self.idnum,self.name,self.description,','.join(str(v) for v in self.color),self.creator,','.join(str(v) for v in self.bookmarks),self.privacy]
    database.setTag(variables)
