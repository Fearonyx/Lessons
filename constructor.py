class Car:
	engine = 'V8-Turbo'

	def __init__(self, requested_color):
		self.color = requested_color


t = Car('red')
t1 = Car('white')


class Tables:

	def __init__(self, number_of_legs):
		print('New table has {} legs'.format(
			number_of_legs))


table = Tables(3)
table1 = Tables(4)


class Chair:
	def __init__(self, color):
		self.color = color


c = Chair('Green')
print(c, c.color)

c1 = Chair('Red')
print(c1.color)
print('Variable {} did not change'.format(c.color))


class Calc(object):
	def __init__(self, number):
		self.number = number

	def calc_and_print(self):
		value = self.calc_value()
		self.print_number(value)

	def calc_value(self):
		return self.number * 10 + 2

	def print_number(self, value_to_print):
		print('----')
		print('Number is ', value_to_print)
		print('----')


class CalcExtraValue(Calc):

	def calc_value(self):
		return self.number - 100


calc = Calc(3)
calc.calc_and_print()

calc2 = CalcExtraValue(101)
calc2.calc_and_print()
