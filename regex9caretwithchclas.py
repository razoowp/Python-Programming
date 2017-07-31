import re

#$ . has no menaing within character classes, ^ at the start of character
#class is used to invert it. ^ has no meaning unless it is the first character in a class.

pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
    print("Match1")

if re.search(pattern, "AbCdEfG123"):
    print("Match2")

if re.search(pattern, "THISISATEXT"):
    print("Match3")

if re.search(pattern, "HELLO HELLO"):
    print("Match5")

'''
Match1
Match2
Match5  ::since there is space it will also match
'''
