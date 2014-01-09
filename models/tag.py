from model import Model

class Tag(Model):
  name = "Default Tag Name"
  description = "Default Tag Description"
  color = [0, 0, 0] # Store color as RGB list, I guess. Probably FIXME
  creator = None # User who created the tag
  bookmarks = [] # Bookmarks with this tag
  privacy = "private" # We probably want something more like an enum here, FIXME
  def __repr__(self):
    return "<Tag %d>"%(self.id)
