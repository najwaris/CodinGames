import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
l = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
array = [r] #to hold the original number of sequence 

#start nested-loop
#outer loop
for i in range(1, l):
    new_array = []
    num, last = 0, -1
    #inner loop
    for j in array:
        if j != last:
            if num != 0:
                new_array.append(num)
                new_array.append(last)
            num = 1
        else:
            num +=1
        last = j
    new_array.append(num)
    new_array.append(last)
    array = new_array
print( ' '.join(str(j) for j in array))
