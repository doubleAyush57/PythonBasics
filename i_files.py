# 'r' = read mode
# 'w' = write mode

fileName = "file.txt"
file = open(fileName, 'r')

f = file.readlines()
print(f)

file = open(fileName, 'w')
file.write("I am learning to write to a file")
file.close()