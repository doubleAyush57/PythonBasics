number = input("enter a number\n")

try:
    value = int(number)
    print(value)
except:
    print("not a valid integer entry")