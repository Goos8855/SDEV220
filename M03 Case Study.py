class Vehicle:
    def __init__(car, vehicle_type):
            car.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(car, vehicle_type, year, make, model, doors, roof):
            super().__init__(vehicle_type)
            car.vehicle_type = vehicle_type
            car.year = year
            car.make = make
            car.model = model
            car.doors = doors
            car.roof = roof
    def printInfo(car):
          clearTerminal()
          print("----- " + car.vehicle_type +" Information -----")
          print(car.year + " " + car.make + " " + car.model)
          print("Number of doors:" + car.doors)
          print("Roof type: " + car.roof)
def clearTerminal():
      for i in range(100):
        print("\n")  

def main():
      
      clearTerminal()
      
      type = "Car"

      year = input("What year was your car made? ")
      make = input("what's the make of your car? ")
      model = input("What's the model of your car? ")
      doors = input("How many doors are on the car? ")
      roof = input("What type of roof does your car have? ")

      car = Automobile(type,year,make,model,doors,roof)
      car.printInfo()

main()