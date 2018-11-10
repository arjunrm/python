s = set()

for i in range(0, 10):
    s.add(i)

print(s)

s2 = s.copy()

print(s2)

for i in range(11,20):
    s.add(i)

print(s)

print(s.difference(s2))

s.intersection_update(s2)
print(s)

print(s.issuperset(s2))

