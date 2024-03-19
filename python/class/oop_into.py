# class MyFirstClass:
#     pass
#
# object_of_my_class = MyFirstClass()
# print(type(object_of_my_class))

# class Car:
#
#     wheels_number = 4
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year =year
#         self.is_crashed = is_crashed
#     def drive(self, city):
#         print(self.name + ' is driving to ' + city)
#
#     def change_color(self, new_color):
#         self.color = new_color
#
# opel_car = Car('Open Tigra', 'grey', '1999', True)
# opel_car.drive('London')
# mazda_car = Car('Mazda SX7', 'green', '2014', False)
# mazda_car.drive('Paris')
# mazda_car.change_color('yellow')
# print(mazda_car.color)


# print(opel_car.wheels_number)
# print(opel_car.name)
# mazda_car = Car(name='Mazda CX7', color='blask', year=1992, is_crashed=True)
#
# print(mazda_car.name, mazda_car.color, mazda_car.year, mazda_car.is_crashed)
# print(mazda_car.wheels_number)
#
# # bmw_car = Car(name='BMW M2')
# #
# # print(bmw_car.name)


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.circumference = 2 * Circle.pi * self.radius

    def get_area(self):
        return self.pi * (self.radius ** 2)

    def get_circumference(self):
        return 2 * self.pi * self.radius

circle_1 = Circle(3)
print(circle_1.get_area())
print(circle_1.circumference)
# circle_2 = Circle(3)
# print(circle_2.get_area())
# circle_3= Circle(5)
# circle_area = circle_3.get_area()
# print(circle_area)