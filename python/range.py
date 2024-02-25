# Задание 1
# list = [3, 2, 1, 0]
# for x in list:
#     print(x)

# Задание 2
guess_me = 7
number = 1
while number <= guess_me:
    if number < guess_me:
        print("too low")
        number += 1
    if number == guess_me:
        print("found it")
        break
        number += 1
else:
    print("oops")
    number += 1