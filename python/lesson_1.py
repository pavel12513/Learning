# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# while True:
#     stuff = input("String to capitalize [type q to quit]: ")
#     if stuff == "q":
#         break  # оператор прерывания. Если на вход подам букву q, цикл завершит свою работу
#     print(stuff.capitalize())

# Пропуск итерации. Оператор continue

# while True:
#     value = input("Integer, please [q to quit]: ")
#     if value == 'q':
#         break
#     number = int(value)
#     if number % 2 == 0: # проверка на нечетное число
#         continue
#     print(f"{number} squares it {number*number}")

# Проверяем, завершился ли цикл раньше, с помощью блока else

# numbers = [1, 3, 5, 4]
# position = 4
# while position < len(numbers):
#     number = numbers[position]
#     if number % 2 == 0:
#         print(f"Found even number, {number}")
#         break
#     position += 1
# else:
#     print("No even number,be found")

# итерация с использование ключевых слов for и in
# word = 'thud'
# offset = 0
# while offset < len(word):
#     print(word[offset])
#     offset +=1
# print("      ")
#
#
# for letter in word:
#     if letter == "u":
#         break
#     print(letter)

# Блок else
word = "txhud"
for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
        break
    print(letter)
else:
    print("No 'x' in there.")