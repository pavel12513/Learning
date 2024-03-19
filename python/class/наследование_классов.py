
class Car:
    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
        print('Car is created')


    def drive(self, city):
        print(self.name + ' is driving to ' + city)

    def change_color(self, new_color):
        self.color = new_color
        print('Color is changed to ' + new_color)

class Truck(Car): # в скобках указываем класс предок, из которого будем тянуть некоторые переменные
    wheels_number = 6
    def __init__(self, name, color, year, is_crashed):
        Car.__init__(self, name, color, year, is_crashed)
        print('Truck is created')

    def drive(self, city):
        print('Truck ' + self.name + ' is driving to ' + city)

man_truck = Truck('Man', 'white', 2015, False)

man_truck.drive('New York')
print(man_truck.wheels_number)

man_car = Car('Mazda CX6', 'white', 2015, False)
print(man_car.wheels_number)

print(man_truck.color)
man_truck.change_color('red')
print(man_truck.color)