# def ten_percent_of_product(x, y, z):
#     return (x * y * z) * 0.1
#
#
# print(ten_percent_of_product(10, 20, 7))


# def ten_percent_of_product_with_args(*args):
#     product = 1
#     for number in args:
#         product =  product * number
#     return product * 0.1
#
#
# print(ten_percent_of_product_with_args(10, 20, 2, 5, 20))


# def percent_of_product_with_args(percent, *args):  # позиционные параметры передаем первые в последовательности
#     product = 1
#     for number in args:
#         product =  product * number
#     return product / 100 * percent
#
#
# print(percent_of_product_with_args(20, 10, 20, 2, 5, 20))

# def func_with_arg(*args):
#     print(args)
#
# print(func_with_arg(1, 2, 3))
#
# def func_with_kwargs(**kwargs):
#     print(kwargs)
#
# func_with_kwargs(first=1, second=2, third=3)

def hello_with_kwargs(**kwargs):
    if 'name' in kwargs:
        print('Hello! Nice to meet you,  {}'.format(kwargs['name']))
    else:
        print('Hello! What is your name? ')

hello_with_kwargs(gender='male', age=24, name='Pavel')
hello_with_kwargs(gender='male', age=24)
