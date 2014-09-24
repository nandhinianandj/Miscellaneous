import fileinput
import math
lines = [3,23,234,10]
#for line in fileinput.input():
#    lines.append(int(line))

def find_sum_of_multiples(count, x):

    res = int()
    n = (count -1) // x
    return x * (n*(n+1)/2)

for each in lines[1:]:
    sum_of_3s = find_sum_of_multiples(each, 3)
    sum_of_5s = find_sum_of_multiples(each, 5)
    sum_of_15s = find_sum_of_multiples(each, 15)
    print(sum_of_3s + sum_of_5s - sum_of_15s)
