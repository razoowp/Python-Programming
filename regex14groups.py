import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match1")

if re.match(pattern, "eggspamspamspamegg"):
    print("Match2")

if re.match(pattern, "spam"):
    print("Match3")

'''
(spam) represents a group in the example pattern shown above

output::

Match1
Match2
'''