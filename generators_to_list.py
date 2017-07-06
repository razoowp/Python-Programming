## Finite generators can be converted into lists by passing them as arguments
## to the list function

def numbers(x):
    for i in range(x):
        if i%2==0:
            yield i

print(list(numbers(15)))

#output:
#[0, 2, 4, 6, 8, 10, 12, 14]
