# Class Making

class Car():
    def __init__(self,carname,carmake,caryear):# it is like a constructor
        self.carname = carname
        self.carmake  = carmake
        self.caryear = caryear
        self.battery = "300amp" # it is a default variable we can also change its value

    def dataofCar(self):
        print("Car Name\tModel\tModel Year\tBattery(AMP)")
        print(self.carname+"\t\t"+self.carmake+"\t\t"+self.caryear+"\t\t"+self.getbatterysize())


    # dunction to update the battery size
    def changebatterysize(self,new_size):
        self.battery = new_size

    # Function to get the battery size
    def getbatterysize(self):
        return self.battery


# Making an object of the car Class
car1 = Car("Audi A5","Audi","2022")
car2 = Car("BMW X5","BMW","2022")

car1.changebatterysize("500amp")
car1.dataofCar()



