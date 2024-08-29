from customer import Customer
from vehicle import *

n = 0

while n != 6:

    print("1. Register a new Customer to buy a car.")
    print("2. Get Customer details.")
    print("3. Get the Customers Vehicle details.")
    print("4. Sell car to the customer.")
    print("5. Buy a car from the customer.")
    print("6. Exit !!!")

    n = int(input("Choose an operation : "))

    if n == 1:
        # name,age,gender,mobileNo,driversLicenceNo,drivingExperience
        name = input("Enter customer name : ")
        age = int(input("Enter customer age: "))
        gender = input("Enter customer gender: ")
        mobileNo = input("Enter customer mobile number: ")
        driversLicenceNo = input("Enter customer driver's license number: ")
        drivingExperience = int(input("Enter customer driving experience in years: "))

        person = Customer(name,age,gender,mobileNo,driversLicenceNo,drivingExperience)
        print(person.__dict__)
        print()

    if n == 2:
        name = input("Enter customer name to display the information : ")
        if Customer.person:
            for i in Customer.person:
                if i.name == name:
                    print(i.__dict__)
                    print("\n")
                    for vehicle in i.vehicles:
                        print(vehicle)

    if n == 3:
        name = input("Enter customer name : ")
        if Customer.person:
            for i in Customer.person:
                if i.name == name:
                    for j in i.vehicles:
                        print(j.__dict__)

    if n == 4:
        name = input("Enter customer name : ")
        if Customer.person:
            for i in Customer.person:
                if i.name == name:
                    m = 0

                    print("Choose your type of Vehicle : \n")
                    print("1. To buy a Commercial vehicle eg : Bike, Car, SUV's.")
                    print("2. TO buy a heavy duty vehicle for Constrution/Transport work eg : Truck, Buldozer, Road Roller")

                    m = int(input("Enter which type of car do you want ? "))
                    print()

                    if m == 1:
                        company = input("Choose the company of the vehicle : ")
                        manufacturingYear = int(input("Enter the manufacturing year of the vehicle : "))
                        fuelCapacity = int(input("Enter the fuel capacity of the vehicle (in liters) : "))
                        noOfDoors = int(input("Enter the number of doors of the vehicle: "))
                        type = input("Enter the type vehicle eg ( Bike,car,SUV's ) : ")
                        mileage = input("Enter the mileage of the vehicle : ")
                        vehicle = LigthMotorVehicle(company,manufacturingYear,fuelCapacity,noOfDoors,type)
                        i.buyVehicle(vehicle)
                        print(vehicle.__dict__)
                        print()
                
                    elif m == 2:
                        company = input("Choose the company of the vehicle : ")
                        manufacturingYear = int(input("Enter the manufacturing year of the vehicle : "))
                        fuelCapacity = int(input("Enter the fuel capacity of the vehicle (in liters) : "))
                        carryingCapacity = int(input("Enter carrying capacity of the vehicle (in kgs) : "))
                        type = input("Enter the type vehicle eg ( Truck, Buldozer, Road Roller ) : ")
                        vehicle = TransportVehicle(company,manufacturingYear,fuelCapacity,carryingCapacity,type)
                        i.buyVehicle(vehicle)
                        print(vehicle.__dict__)
                        print()

        print("Persons not found\n")

    if n == 5:
        name = input("Enter a name : ")
        if Customer.person:
            for i in Customer.person:
                if i.name == name:
                    print("You can sell your vehicle : ")

                    for index,value in enumerate(i.vehicles):
                        print(index,value.__dict__)

                        indexNumber = int(input("Which car do you want to sell : "))
                        if 0 <= indexNumber < len(i.vehicles):    
                            # number = i.vehicles[indexNumber]
                            i.sellVehicle(i.vehicles[indexNumber])
                            print("Sold Successfully")
                            for k in i.vehicles:
                                print(k.__dict__)

                    