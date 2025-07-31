class car:
    def __init__(self, colour, name):
        self.colour = colour
        self.name = name

    def car_specs(self, speed, weight):
        print(f"{speed} km/h {weight} kg")
        
car1= car("red", "ferrari")
car2= car("white", "bmw")

print(car1.colour)
print(car2.name)

car1.car_specs(200, 1500)
car2.car_specs(180, 1400)


#
class flower:
    def __init__(self, colour, name):
        self.colour = colour
        self.name = name

    def flower_specs(self, height, fragrance):
        print(f"{height} cm {fragrance} scent") 

flower1 = flower("white", "rose")
flower2 = flower("blue", "lily")

print(flower1.colour)
print(flower2.name)

flower1.flower_specs(30, "sweet")
flower2.flower_specs(25, "fresh")

# class method
class car:
    wheels=4
    @classmethod
    def update_wheels(cls,count):
        cls.wheels = count

car.update_wheels(6)  
print(car.wheels)

#static method
class car:
    @staticmethod
    def greet():
        print("Hello, welcome to the car showroom!")
car.greet()

#remove special characters 
s="kiets@123"
output=s.replace("@", "")
print(output)

#write a python program to print second largest number from a list(without using sort(),max())
numbers= [10, 20, 4, 45, 99, 99, 45]
def second_largest(numbers):
    first = second = float('-inf')
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif number > second and number != first:
            second = number
    return second


