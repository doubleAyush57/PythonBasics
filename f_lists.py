fruits = []

for i in range (0, 5):
    fruits.append(input("Name a fruit\n"))

print(fruits)

fruits.remove(fruits[0])
print(fruits)
