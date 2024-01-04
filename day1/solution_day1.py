import re
t = 0
n = "one two three four five six seven eight nine ten".split()
p = "|".join(n) + "|\d"
# 9zngoneoneightzdz
# ['9', '1', '1']

# this "positive lookahead" or zero-width assertion looks after "oneight" 
p = "(?=(" + p + "))"
# 9zngoneoneightzdz
# ['9', '1', '1', '8']


# p = "(?=(one|two|three|four|five|six|seven|eight|nine|ten|\d))"
print(p)
def f(x):
    if x in n:
        return str(n.index(x)+1) 
    return str(int(x))

for x in open(0):
    digits = [*map(f, re.findall(p, x))] 
    print(f"{x}:{digits}")
    t += int(digits[0] + digits[-1])
    print(t)
