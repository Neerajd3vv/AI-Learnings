age = 21
salary = 100000
skills = ["Python", "JavaScript", "SQL"]
details = {"city": "New York", "job": "Developer"}

# // print

print("Age:", age)
print("Salary:", salary)
print("Skills:", skills)
print("Details:", details)



skills3 = skills.copy()

print("Skills copy:", skills3)
skills2 = skills
skills2.append("Java")
print("Skills after modification:", skills)

# Things to remember #
# 1. four white spaces
# 2. everything in the python is the object, unlike JS where Primitives like: number string boolean null undefined symbol bigint are NOT objects (they are primitive values). But then… why can we do this in JS? "hello".toUpperCase() -> JavaScript temporarily wraps primitives into objects behind the scenes using wrapper objects, This process is called boxing.
# 3. python variable are assigned by reference.
    # list1 = [1,2,3]
    # list2 = list1

    # list2.append(4)

    # print(list1)  # [1,2,3,4]  <- reference copy

    # If you want value copy:
    # list2 = list1.copy()
# 4. f-strings for string interpolation.

print(f"My name is Neeraj and I am {age} years old.")
