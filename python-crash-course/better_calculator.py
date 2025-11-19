num_1 = float(input("Enter your first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num_2 = float(input("Enter your second number: "))


if operator == "+":
    print(f"{num_1} + {num_2} = {num_1 + num_2}")
elif operator == "-":
    print(f"{num_1} - {num_2} = {num_1 - num_2}")    
elif operator == "*":
    print(f"{num_1} * {num_2} = {num_1 * num_2}")
elif operator == "/":
    print(f"{num_1} / {num_2} = {num_1 / num_2}")
else:
    print("Invalid operator!")            
