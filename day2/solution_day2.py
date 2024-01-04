t = 0
for i, x in enumerate(open(0)):
    gs = x.strip().split(': ')[1].split('; ')
    d = {'red': 0, 'green': 0, 'blue': 0} 
    for g in gs:
        g = g.split(', ')
        print(g)
        for e in g:
            v, k = e.split()
            # print(f"checking {e}")
            d[k] = max(d[k], int(v))
    lt = 1
    for k in d:
        lt *= d[k]

    t += lt
    print(t)
