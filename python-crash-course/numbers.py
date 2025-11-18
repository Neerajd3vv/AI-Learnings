# int -> integer/ whole number, float -> decimal number

print(3 * 4 + 5)  # arithmetic operations
print(3 * (4 + 5))  # we can change the order of operations using parentheses
print(10 / 3)  # division -> 3.333333333
print(10 // 3)  # floor division -> 3 -> removes decimal part
print(10 % 3)  # modulus

age = 23
# print("My age is: " + age ) # Js would have done this by doing type coersion
print("My age is:" + str(age))  # type casting in python

# Bunch of methods on the number

print(abs(-7))  # absolute value
print(pow(3, 2))  # power -> 3^2 = 9
print(max(4, 6))  # maximum
print(min(4, 6))  # minimum 
print(round(7.8))  # rounding off

import math
print(math.floor(9.8))  # floor value -> 7
print(math.ceil(9.2))  # ceil value -> 10
print(math.sqrt(64))  # square root -> 8.0