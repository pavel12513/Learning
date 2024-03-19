# class Car:
#     def __init__(self, name):
#         self.name = name
#
# furball = Car('Grumpy')
# print(furball.name)

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
    def need_a_push(self):
        print('A little help here?')

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_yugo.need_a_push()


#
# class Person():
#     def __init__(self, name):
#         self.name = name
#
# class MDPerson(Person):
#     def __init__(self, name):
#         self.name = "Doctor " + name
#
# class JDPerson(Person):
#     def __init__(self, name):
#         self.name = name + " , Esquire"
#
# person = Person('Pavel')
# doctor = MDPerson('Pavel')
# lawyer = JDPerson('Pavel')
# print(person.name)
# print(doctor.name)
# print(lawyer.name)