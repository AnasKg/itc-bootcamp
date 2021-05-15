
class Laptop:
	def __init__(self, model_name):
		self.model = model_name
		self.harakteristiki = {'model': model_name}
		self.processor()
		self.ram()
		self.video_card()
		self.hdd()
		self.motherboard()
		self.display_size()

	def processor(self):
		self.harakteristiki['processor'] = 'Core i 123'

	def ram(self):
		self.harakteristiki['ram'] = '16 gb'

	def video_card(self):
		self.harakteristiki['video_card'] = '4 gb'

	def hdd(self):
		self.harakteristiki['hdd'] = '1024 gb'

	def motherboard(self):
		self.harakteristiki['motherboard'] = 'asdasdasd'

	def display_size(self):
		self.harakteristiki['display_size'] = '27 d'


laptop = Laptop(model_name='Acer')
print(laptop.model)
print(laptop.harakteristiki)




