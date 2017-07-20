import re
pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match1")

if re.match(pattern, "gray"):
    print("Match2")

if re.match(pattern, "blue"):
    print("Match3")

'''
    Match1
    Match2
'''

    
