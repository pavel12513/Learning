simple_string = "Hello, world"
byte_string = b"Hello, world"
byte_array_strinf = bytearray(byte_string)


print(byte_string)
print(type(simple_string))
print(type(byte_string))
print(type(byte_array_strinf))


name = "John"
byte_name = name.encode("UTF-8") # закодируем в байты при помощи UTF-8
print(type(byte_name))