#******************************************#
#This is generators sample code

def countdown():
    i = 5
    while i>0:
        yield i
        i -= 1

for i in countdown():
    print(i)

#output
#    5
#    4
#    3
#    2
#    1

#*******************************************#
#Generators can be infinite

def infinite_sevens():
    while True:
        yield 7

for i in infinite_sevens():
    print(i)

#This will print infinite 7...

    
