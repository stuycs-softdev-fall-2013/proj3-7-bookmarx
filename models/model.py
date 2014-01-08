# All actual models should subclass this
# Avoid circular references at all costs.
class Model(object):
  id = 0
  def __init__(self):
    self.load()
  def __del__(self):
    self.unload()
  def __repr__(self):
    return "<Model %d>"%(self.id);
  # This should be overrided by a subclass to provide DB load
  # It will be automatically called in the constructor
  def load(self):
    print "birth"
  # This should be overrided by a subclass to provide DB unload
  # It will be automatically called in the destructor
  def unload(self):
    print "death"

if __name__ == '__main__':
  m = Model()
  print "stuff happens here"
