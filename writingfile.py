file = open("para.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("para.txt", "r")
print(file.read())
file.close()