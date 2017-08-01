import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match1")

if re.match(pattern, "eggspamspamegg"):
    print("Match2")

if re.match(pattern, "spam"):
    print("Match3")

'''
    Match1
    Match2
'''