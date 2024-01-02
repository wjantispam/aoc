seeds, *blocks = open(0).read().split("\n\n")
print(f"{blocks}")


seeds = list(map(int, seeds.split(':')[1].split())) 

for block in blocks:
    for line in block.splitlines():
        print(line)
        for x in seeds:
            for a, b, c in ranges:
                if b <= x < b+c:


