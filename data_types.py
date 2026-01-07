#String subscripting
my_string = "Hello, World!"
first_character = my_string[0]
print(first_character)  # Output: H

last_character = my_string[-1] # This means to get the last character in the string
print(last_character)  # Output: !

#Integer = Whole Division
my_integer = 10
print(my_integer)  # Output: 10

#Large Integers
large_integer = 12345678901234567890
print(large_integer)  # Output: 12345678901234567890

#Float = Decimal Numbers
my_float = 3.14
print(my_float)  # Output: 3.14

#Boolean = True or False
my_boolean = True
print(my_boolean)  # Output: True

#Type Check
print(type(my_string))   # Output: <class 'str'>
print(type(my_integer))  # Output: <class 'int'>
print(type(my_float))    # Output: <class 'float'>
print(type(my_boolean))  # Output: <class 'bool'>

#Type Conversion
string_to_integer = int("123")
print(string_to_integer)  # Output: 123
integer_to_string = str(456)
print(integer_to_string)  # Output: "456"
float_to_integer = int(7.89)
print(float_to_integer)  # Output: 7
integer_to_float = float(123)
print(integer_to_float)  # Output: 123.
boolean_to_integer = int(True)
print(boolean_to_integer)  # Output: 1