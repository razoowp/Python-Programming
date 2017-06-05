#Method-1
f = open("example.csv","r")
data = f.read()
rows = data.split("\n")
for row in rows:
    print(row)
f.close()

"""
Output::
1/2/2014,5,8,red
1/3/2014,5,6,green
2/4/2014,8,0,blue
"""

#Method-2
import csv
with open("example.csv") as f:
    readcsv = csv.reader(f,delimiter=",")

    for row in readcsv:
        print(row)

"""
Output:
['1/2/2014', '5', '8', 'red']
['1/3/2014', '5', '6', 'green']
['2/4/2014', '8', '0', 'blue']
"""

#Making seperate lists of dates and colors and assigning respective values
with open("example.csv") as f:
    readcsv = csv.reader(f,delimiter=",")
    dates=[]
    colors=[]
    for row in readcsv:
       dates.append(row[0])
       colors.append(row[3])
    print(dates)
    print(colors)

"""
Output:
['1/2/2014', '1/3/2014', '2/4/2014']
['red', 'green', 'blue']
"""

## Accessing corresponding Values
whatcolor = input("Enter the color to find the corresponding dates")
getIndex = colors.index(whatcolor.lower())
print("The corresponding date of", whatcolor.lower(), "is: ", dates[getIndex])
