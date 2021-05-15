

class Java:
	def __init__(self):
		self.name = 'Java'
		self.paradigms = 'OOP'
		self.language_type = 'Compiled'
		self.__speed = 300

	def create_desktop(self):
		return f'Я {self.name} могу создовать Desktop программы.'

	def create_game(self):
		return f'Я {self.name} могу создовать игры'

	def create_site(self):
		return f'Я {self.name} могу создовать сайты'

	def get_speed(self):
		return self.__speed


class Python(Java):
	def __init__(self):
		Java.__init__(self)
		self.name = 'Python'
		self.language_type = 'Interpretated'
		self.__level = 'High level'

	def get_level(self):
		return self.__level




j = Java()
print(j.name)
print(j.create_site())
print(j.get_speed())

p = Python()
print(p.get_level())
print(p.name)
print(p.create_site())
print(p.paradigms)
p.paradigms = ['OOP', 'Functional']
print(p.paradigms)
p.speed = 100
print(p.speed)




