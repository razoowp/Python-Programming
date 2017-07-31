import re

pattern = r"[A-Z][A-Z][0-9]"  

if re.search(pattern, "LS8"):
    print("Match1")

if re.search(pattern, "E3"):
    print("Match2")

if re.search(pattern, "lab"):
    print("Match3")

if re.search(pattern, "hkjlkHN6kjlk"):  #Sequential aauna paryo pattern anusar
    print("Match4")

if re.search(pattern, "hkjlkHNk6"):
    print("Match5")

'''
output:
Match1
Match4
'''
    
