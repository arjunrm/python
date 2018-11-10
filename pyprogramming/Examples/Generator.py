def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes)

# generates value when queried so doesn't store in memory
# need to iterate through the function to get all the values
# similar to range()
def create_cubes_gen(n):
    for x in range(n):
        yield x**3

for x in create_cubes_gen(10):
    print(x)

def fibonacci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

print('')
for num in fibonacci(10):
    print(num)

fibo = fibonacci(5)
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))

s = 'Sample'
s_itr = iter(s)
print(next(s_itr))
print(next(s_itr))
print(next(s_itr))
print(next(s_itr))

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

