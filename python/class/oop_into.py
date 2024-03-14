# class MyFirstClass:
#     pass
#
# object_of_my_class = MyFirstClass()
# print(type(object_of_my_class))

class Car:

    wheels_number = 4
    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year =year
        self.is_crashed = is_crashed

mazda_car = Car(name='Mazda CX7', color='blask', year=1992, is_crashed=True)

print(mazda_car.name, mazda_car.color, mazda_car.year, mazda_car.is_crashed)
print(mazda_car.wheels_number)

# bmw_car = Car(name='BMW M2')
#
# print(bmw_car.name)