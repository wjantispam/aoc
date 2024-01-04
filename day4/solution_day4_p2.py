#!/usr/bin/env python3
# Part One
def part_one():
    t = 0
    for i, x in enumerate(open(0)):
        x = x.strip().split(':')[1]
        # a, b = x.split(' | ')
        # a = list(map(int, a.split()))
        a, b = [list(map(int, k.split())) for k in x.split(' | ')]
        d = sum([q in b for q in a])
        if d > 0:
            t += pow(2, d-1)
    print(f"{t}")
    # print(f"{a}, {b}")


# Part Two
t = 0
m = {}
for i, x in enumerate(open(0)):
    if i not in m:
        m[i] = 1
    x = x.strip().split(':')[1]
    a, b = [list(map(int, k.split())) for k in x.split(' | ')]
    d = sum([q in b for q in a])
    for n in range(i+1, i+d+1):
        m[n] = m.get(n, 1) + m[i]
    print(f"{m}")
print(sum(m.values()))

if __name__ == '__main__':
    # part_one()
    print("Run main")
