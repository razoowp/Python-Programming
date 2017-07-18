import re
pattern = r"pam"

match = re.search(pattern, "eggpamsausage")

if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())


    #output
    '''
    pam
    3
    6
    (3, 6)

    '''
    
