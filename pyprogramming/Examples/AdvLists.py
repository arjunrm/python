l1 = [x for x in range(10)]
print(l1)

l1.append([4, 5])
print(l1)

l1.extend([x for x in range(5,15)])
print(l1)

print(l1.index([4,5]))

l1.insert(l1.index([4,5]), 99)
print(l1)

l1.remove([4,5])
print(l1)

l1.reverse()
print(l1)

l1.sort()
print(l1)


