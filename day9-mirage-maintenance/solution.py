#!/usr/bin/env python3
def extrapolate(array):
    if all(x == 0 for x in array):
        return 0
    
    deltas = [y-x for x, y in zip(array, array[1:])]
    diff = extrapolate(deltas)
    return array[-1] + diff

total = 0

print(extrapolate([1,3,6,10,15,21]))

for line in open(0):
    nums = list(map(int, line.split()))
    total += extrapolate(nums)

print(total)