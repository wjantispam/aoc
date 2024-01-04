t = 0
for i, x in enumerate(open(0)):
    x = x.strip().split(':')[1]
    # a, b = x.split(' | ')
    # a = list(map(int, a.split()))
    a, b = [list(map(int, k.split())) for k in x.split(' | ')]
    d = sum([q in b for q in a])
    print(f"{d}")
    if d > 0:
        t += pow(2, d-1)
print(f"{t}")
# print(f"{a}, {b}")
