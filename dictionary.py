#creation of dictionary and accessing it
ages = {"raju":28, "keddar":23, "hari":31}
print(ages["keddar"])
print(ages["raju"])

#Assisgning values to dictionary keys with different values
squares = {1:1, 2:4, 3:"error", 4:16,}
squares[8] = 64
squares[3] = 9
print(squares)

#To determine whether a key is in a dictionary

nums = {
    1:"one",
    2:"two",
    3:"three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)