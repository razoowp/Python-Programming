import re

pattern = r"[a,e,i,o,u]"

if re.search(pattern, "grey"):
    print("Match1")

if re.search(pattern, "qwertyuiop"):
    print("Match2")

if re.search(pattern, "rhythm myths"):
    print("Match3")

    
'''
output:
Match1
Match2
'''
