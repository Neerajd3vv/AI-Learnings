super_heros = ["spiderman", "ironman", "thor", "hulk", "captain america", "hulk"]

print(super_heros[0])  # Output: spiderman
print(super_heros[1:])
print(super_heros[1:4]) 

# funtions with arrays

lucky_numbers = [4, 8,  16, 15, 23, 42]
# super_heros.extend(lucky_numbers)
super_heros.append("black panther")
print(super_heros)

super_heros.insert(1, "doctor strange")
print(super_heros)

super_heros.remove("thor")
print(super_heros)

# super_heros.clear()
print(super_heros)


lucky_numbers.pop()
print(lucky_numbers)

print(super_heros.index("hulk"))

print(super_heros.count("hulk"))


super_heros.sort()
print(super_heros)

print(sorted(lucky_numbers)) # This will not change the original list, creates the copy of it -> sorted it and return it

print(lucky_numbers)

lucky_numbers.sort()
print(lucky_numbers) # This will change the original list

lucky_numbers.reverse()
print(lucky_numbers)

super_heros_2 = super_heros.copy()
super_heros_2.append("test")
print(super_heros_2)
print(super_heros)