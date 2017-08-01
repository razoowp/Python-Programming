import re

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")

if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print(match.group(4))
    print(match.groups())

'''
abcdefghi
abcdefghi
bc
de
fgh
g
('bc', 'de', 'fgh', 'g')

'''