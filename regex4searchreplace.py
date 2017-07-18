import re

str = "My name is Raju. Hi Raju"
pattern = r"Raju"

newstr = re.sub(pattern, "Krishna", str)
print(newstr)
