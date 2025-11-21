
try:
    # number = 10/0
    number = int(input("Enter a number: "))
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input. Please enter a valid number.")

# try:
#     # number = 10/0
#     number = int(input("Enter a number: "))
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print(err)        

