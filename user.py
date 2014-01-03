class User:
	def __init__(self, name, password):
		self.name = name
		self.password = encrypt(password)
		self.tags = []
		self.bookmarks = []
	def __del__(self):
		pass
		# save self to database

def encrypt(password):
	return "1%s"%password
