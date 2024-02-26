
class Credit_operation:
    def __init__(self):
        self.vehicle_value:float 
        self.months:int
        self.tax:float



class Vehicle_financing:
    def __init__(self, credit_operation:Credit_operation):
        self.credit_operation = credit_operation


    def calculate_financing_slices(self):
        return ("Total to be paid: " + str( self.credit_operation.vehicle_value + (self.credit_operation.vehicle_value * ((self.credit_operation.tax/100) * self.credit_operation.months))))



credit_operation = Credit_operation()
credit_operation.vehicle_value = 10000
credit_operation.months = 12
credit_operation.tax = 1.0


vehicle_financing = Vehicle_financing(credit_operation)
print(vehicle_financing.calculate_financing_slices())
