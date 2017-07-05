#Map program
#The function map takes a function and an iterable as arguments, and returns
#a new iterable with the function applied to each argument.

def add_five(x):
    return x+5

nums = [5,6,7,8,9]
result = list(map(add_five,nums))
print(result)

#output: [10,11,12,13,14]
##***************************************************##
## The above code in lambda ##

result = list(map(lambda x:x+5, nums))
print("Using Lambda:", result)
