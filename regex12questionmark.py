import re

pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
    print("Match1")

if re.match(pattern, "icecream"):
    print("Match2")

if re.match(pattern, "ice--cream"):
    print("Match3")

if re.match(pattern, "sausages"):
    print("Match4")

'''
Match1
Match2
'''