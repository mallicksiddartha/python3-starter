import statistics

example_list = [1, 2, 3, 4, 5, 6, 7, 8, 12, 78, 45, 95]

x = statistics.mean(example_list)
y = statistics.median(example_list)
z = statistics.stdev(example_list)
xx = statistics.variance(example_list)
print(x)
print(y)
print(z)
print(xx)

