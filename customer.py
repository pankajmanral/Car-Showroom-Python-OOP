from vehicle import Vehicle

class Customer:

    person = []

    def __init__(self,name,age,gender,mobileNo,driversLicenceNo,drivingExperience) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.mobileNo = mobileNo
        self.driversLicenceNo = driversLicenceNo
        self.drivingExperience = drivingExperience
        self.vehicles = []
        Customer.person.append(self)

    def buyVehicle(self,vehicle):
        self.vehicles.append(vehicle)

    def sellVehicle(self,vehicle):
        self.vehicles.remove(vehicle)
