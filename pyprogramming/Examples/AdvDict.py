d1 = {'k1':1, 'k2':2}

d2 = {x:x**2 for x in range(10)}
print(d2)

d3 = {k:v**2 for k,v in zip(['a', 'b'], range(2))}
print(d3)

for k,v in d2.items():
    print(k,v)

