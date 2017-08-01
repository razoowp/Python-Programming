import re

pattern = r"g+"

if re.match(pattern, "g"):
    print("Match1")

if re.match(pattern, "ggggggggg"):
    print("Match2")

if re.match(pattern, "abc"):
    print("Match3")

'''
Match1
Match2

'''