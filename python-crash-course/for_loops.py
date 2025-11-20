for index in range(10):
    print(index)
for index in range(3,10):
    print(index)

for letter in "Python":
    print(letter)    

super_heros = ["spiderman", "ironman", "thor", "hulk"]
for super_hero in super_heros:
    print(super_hero.title())


for index in range(len(super_heros)):
    print(f"{index}: {super_heros[index].title()}")