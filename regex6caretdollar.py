import re 

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match1")

if re.match(pattern, "gray"):
    print("Match2")

if re.match(pattern, "stingray"):
    print("Match3")

if re.search(pattern, "stingray"):
    print("Match4")

#Understand the relation of ^ and .match in above code
pattern2 = r"gr.y$"

if re.search(pattern2, "stingray"):
    print("Match5")

'''
output:
Match1
Match2
Match5
'''
