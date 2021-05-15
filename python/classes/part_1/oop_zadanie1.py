
class Laptop:
	def __init__(self, model_name):
		self.model = model_name
		self.harakteristiki = []
		self.processor()
		self.ram()
		self.video_card()
		self.hdd()
		self.motherboard()
		self.display_size()

	def processor(self):
		self.harakteristiki.append('Corei 8')

	def ram(self):
		self.harakteristiki.append('16 gb')

	def video_card(self):
		self.harakteristiki.append('4 gb')

	def hdd(self):
		self.harakteristiki.append('1024 gb')

	def motherboard(self):
		self.harakteristiki.append('Asdasd')

	def display_size(self):
		self.harakteristiki.append('27 d')


laptop = Laptop(model_name='Asus')
print(laptop.model)
print(laptop.harakteristiki)




