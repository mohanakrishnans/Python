# from file_name import class_name 
from Vehicle import Vehicle 
class Truck(Vehicle):
	def __init__(self,year ,model, plate_number,current_speed,current_cargo):
		super().__init__(year,model,plate_number,current_speed)
		self.current_cargo = current_cargo

	def add_cargo(self,cargo):
		self.current_cargo += cargo

	def remove_cargo(self, cargo):
		self.current_cargo -= cargo

