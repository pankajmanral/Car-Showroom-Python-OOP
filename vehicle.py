class Vehicle:
    def __init__(self,company:str,manufacturingYear:int,fuelCapacity:int) -> None:
        self.company = company  
        self.manufacturingYear = manufacturingYear
        self.fuelCapacity = fuelCapacity

class LigthMotorVehicle(Vehicle):
    def __init__(self, company: str, manufacturingYear: int, fuelCapacity: int,noOfDoors: int,type: str,mileage:int) -> None:
        super().__init__(company, manufacturingYear, fuelCapacity)
        self.noOfDoors = noOfDoors
        self.type = type
        self.mileage = mileage

    def __str__(self):
        return f'{self.company}{self.manufacturingYear}{self.fuelCapacity}{self.noOfDoors}{self.type}{self.mileage}'

class TransportVehicle(Vehicle):
    def __init__(self, company: str, manufacturingYear: int, fuelCapacity: int, carryingCapacity:int, type:str) -> None:
        super().__init__(company, manufacturingYear, fuelCapacity)
        self.carryingCapacity = carryingCapacity
        self.type = type

    def __str__(self):
        return f'{self.company}{self.manufacturingYear}{self.fuelCapacity}{self.carryingCapacity}{self.type}'
