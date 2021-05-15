

class Car:

	def __init__(self, marka, color, year, model):
		self.marka = marka
		self.color = color
		self.year = year
		self.model = model

	def __str__(self):
		return f'{self.marka} {self.model} {self.color}'

	def drive(self):
		return f'{self.marka} и Я еду'

	def my_method(self):
		print(self.marka)
		self.drive()




car1 = Car(marka='Mers', color='Black', year=2020, model='222')
second_car = Car('Toyota', 'Red', 2021, 'Camry')

print(car1)
print(second_car)
print(second_car.drive())



