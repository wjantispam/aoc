#!/usr/bin/env python3
seeds, *blocks = open(0).read().split('\n\n')

seeds = list(map(int, seeds.split(':')[1].split()))

#print(blocks)
for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    # print(f"list of ranges is \n{ranges}")
    for x in seeds:
        for a, b, c in ranges:
            if b <= x < b+c:
                new.append(x - b + a)
                #print(f"checking {x}, new = {new}")
                break
        else:
            new.append(x)
        
    seeds = new

print(f"{min(seeds)}")
