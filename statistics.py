import statistics
list = [2,3,4,5,6,7,8,9,3,4,5,6,13,45,63,4,66,2]
x = statistics.mean(list)
y = statistics.median(list)
z = statistics.stdev(list)
a = statistics.variance(list)
print(x)
print(y)
print(z)
print(a)

#we can also directly import functions of modules and use directly like this:

from statistics import mean, variance
meanValue = mean(list)
print("MeanValue: ", meanValue)