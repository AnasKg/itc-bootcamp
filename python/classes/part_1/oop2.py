
class Group:

	def __init__(self, name, students):
		self.name = name
		self.students = students
		self.amount = self.get_amount_of_students()

	def __str__(self):
		return f'{self.name} {self.amount}'

	def get_amount_of_students(self):
		amount = len(self.students)
		return amount


group1 = Group('Python3', ['Bermet', 'Aelita', 'Yrys', 'Maksim'])

print(group1.students)
print(group1.amount)
print(group1.get_amount_of_students())

group2 = Group('Вторая группа', ['Oskar', 'Sezim', 'Вы'])
print(group2.students)



