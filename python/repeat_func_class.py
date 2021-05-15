

# my_list = [1, 4,6, 7, 'Python']
# def length():

# 	result = 0
# 	for _ in my_list:
# 		result += 1

# 	print(f'Количество элементов в массиве {result}')

# length()


# def add():
# 	a = 10
# 	b = 20
# 	res = a + b
# 	return res

# result_of_function = add()
# print(result_of_function)


# def subtract(number_1, number_2, num_3=100):
# 	subt = (number_1 - number_2) * num_3
# 	return subt

# res = subtract(10, 3, 7)
# print(res)


# def list_appender(list1, list2, *args, **kwargs):
# 	print(list1)
# 	print(list2)
# 	print(args)
# 	print(kwargs)

# list_appender(1, 2, 400, 5000, name='Python', age=20)


# def decrement(number):
# 	print(number)
# 	if number == 0:
# 		return number
# 	else:
# 		decrement(number-3)

# decrement(21)





# my_func = lambda a, b: a+b
# print(my_func(10, 30))


# def my_decorator(some_function):
# 	def wrapper():
# 		res = some_function()
# 		result = f'{res} World!'.upper()
# 		return result

# 	return wrapper

# @my_decorator
# def hello():
# 	return 'Hello'

# print(hello())



class Weapon:

	def __init__(self, name, classes, speed):
		self.name = name
		self.classes = classes
		self.speed = speed

	def shoot(self):
		return f'{self.name} shoot'


	def __str__(self):
		return f'{self.name} {self.classes}'


w = Weapon(name='Ak-47', classes=['asfads',' asdasd'], speed=300)
print(w.__dict__)

weapon2 = Weapon(name='Glock', classes=['asd'], speed=134)
print(weapon2.__dir__())



