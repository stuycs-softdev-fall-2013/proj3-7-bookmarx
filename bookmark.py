class Bookmark:
	def __init__(self, name, link):
		self.name = name
		self.link = link
		self.tags = []
	def __del__(self):
		#save self to database
		pass
