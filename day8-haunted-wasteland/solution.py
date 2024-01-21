#!/usr/bin/env python3
step, _, *rest = open(0).read().splitlines()

network = {}

for line in rest:
    pos, targets = line.split(" = ")
    network[pos] = targets[1:-1].split(", ")
print(step)
print(network)

step_count = 0
current = "AAA"

while current != "ZZZ":
    step_count += 1
    current = network[current][0 if step[0] == "L" else 1]
    step = step[1:] + step[0]

print(step_count)