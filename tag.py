class Tag:
	def __init__(self, name):
		self.name = name
		self.color = 0x0000ff
	def __del__(self):
		#save self to database
		pass
