from collections import Counter

l = [1,1,1,2,2,4,546,61,54,6,7,8,8,9,99]
c = Counter(l)
print(c)

s = 'How many times the words show up in this words string'
words = s.split()
c2 = Counter(words)
print(c2.most_common(2))
print(c.most_common(4))

from collections import defaultdict

d = {'k1':1, 'k2':2}
print(d['k1'])

dd = defaultdict(lambda: 0)
dd['1']
print(dd)

from collections import OrderedDict

nd = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}
nd[10] = 'h'
nd[7] = 'i'
nd[11] = 'j'
nd[12] = 'k'
for k,v in nd.items():
    print(k,v)


from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')

sam = Dog(age = 2, breed = 'Lab', name = 'Sammy')
print(sam.age)

d2 = Dog
d2.age = 10
d2.breed = 'Lab'
d2.name = 'D2'

class Cat(namedtuple('Cat', 'age name')):
    def __str__(self):
        return f'{self.age} {self.name}'

c1 = Cat(20, 'Spyder')
c2 = Cat(15, 'Python')

print(c1)
print(c2)


