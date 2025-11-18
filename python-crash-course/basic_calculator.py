num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(num1 + num2) # 33 as by default the input function takes input as string
print(int(num1) + int(num2)) # -> int will complain if user enters decimal numbers
print(float(num1) + float(num2)) 