
Result = []
class CarModels:
    def main(self, brand,segment,HorsePower,color):
        self.brand = brand
        self.segment = segment
        self.HorsePower = HorsePower 
        self.color = color

    def description(self):
        print(f"Model is : {self.brand}")
        print(f"Segment is : {self.segment}")
        print(f"Horse Power is : {self.HorsePower}")
        print(f"color is : {self.color}")

CarModel1 = CarModels("Benz", "Hatchback",1600,"Navy Blue")
CarModel2 = CarModels("BMW","SUV",1800,"Green")

CarModel1.description()
CarModel2.description()

#print(list1,list2)
#print(CarModel1)
