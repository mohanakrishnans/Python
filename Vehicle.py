class Vehicle:
    def __init__(self, year, model, plate_number, current_speed = 0):
        self.year = year
        self.model = model
        self.plate_number = plate_number
        self.current_speed = current_speed
        
    def move(self):
        self.current_speed += 1
        
    def accelerate(self, value):
        self.current_speed += value
    
    def stop(self):
        self.current_speed = 0
        
    def vehicle_details(self):
        return self.model + ',' + str(self.year) + ',' + self.plate_number
    