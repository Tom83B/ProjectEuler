week_day = {}

class date:
	def __init__(self, day, month, year, week_day):
		self.day = day
		self.month = month
		self.year = year
		self.week_day = week_day

	def __leapyear__(self):
		if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
			return True
		else: return False

	def __daysinmonth__(self):
		days = [31,28,31,30,31,30,31,31,30,31,30,31]
		if self.__leapyear__(): days[1] = 29
		return days[self.month-1]

	def add_days(self, ddays):
		self.day += ddays
		if self.day+ddays>self.__daysinmonth__():	#nezahrnuje preskoceni celeho mesice
			self.day -= self.__daysinmonth__()
			self.month += 1
			if self.month>12:
				self.month -= 12
				self.year += 1	#nezahrnuje preskoceni celeho roku
		self.week_day += ddays
		self.week_day = self.week_day % 7	# 0: pondeli, 6: nedele

mydate = date(1, 1, 1900,0)
mydate.add_days(365) #1900 neni prestupny, je tedy 1.1.1901
while mydate.week_day != 6: mydate.add_days(1)	#a ted je nedele

SundaysOnFirst = 0

while mydate.year != 2001:
	if mydate.day == 1: SundaysOnFirst += 1
	mydate.add_days(7)

print(SundaysOnFirst)
