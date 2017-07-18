import re

pattern = r"spam"

if re.match(pattern, "eggsspamsausagespam"):
    print("Match")
else:
    print("No Match")

if re.search(pattern, "eggsspamsausagespam"):
    print("Match")
else:
    print("No Match")

print(re.findall(pattern, "eggsspamsausagespam"))

#The function re.finditer does the same thins as re.findall except it returns an
#iterator rather than a list.

print(re.finditer(pattern, "eggsspamsausagespam"))
