with open("para.txt") as f:
   print(f.read())

#The file is automatically closed at the end of the with statement, even if exceptions occur within it.

# Another way to close file is using : finally block as it runs whether or not exception occurs like this:
try:
   f = open("para.txt")
   print(f.read())
finally:
   f.close()