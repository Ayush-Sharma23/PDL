class car:

	make = ""
	model = ""
	year = ""

	def company(self, make):
		self.make = make

	def model(self, model):
		self.model = model

	def year(self,year):
		self.year = year

	def printInfo(self):
		print(f"Car Name : {self.model}\nMade by {self.make} was produced in the year {self.year}")

car1 = car();
car1.company("TATA")
car1.model("Punch")
car1.year("2022")
car1.printInfo()