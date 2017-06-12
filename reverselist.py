list = [4,5,6,7,8,9,23,45,54,2,34,56]

#Method-1 :: this will print output as list
print(list[::-1])

#Method-2 :: this will print output without list in new line
mylist = [9,0,5,6,34,5]
for i in reversed(mylist):
    print(i)


# If we want to keep the reverse list as new list we need to code like this:
mylist = [9,0,5,6,34,5]
newlist=[]
for i in reversed(mylist):
    newlist.append(i)
print(newlist)