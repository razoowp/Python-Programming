import re

pattern = r"9{1,3}$"


if re.match(pattern, "9"):
    print("Match1")

if re.match(pattern, "999"):
    print("Match2")

if re.match(pattern, "9999"):
    print("Match3")


'''
Match1
Match2
'''