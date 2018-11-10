#map function
def square(num):
    return num**2

myNum = [1,2,3,4,5]

squaredList = list(map(square,myNum))
print(squaredList)

#filter function
def checkEven(num):
    return num%2 == 0

eventNums = list(filter(checkEven, myNum))
print(eventNums)

#lambda function
squaredLambaList = list(map(lambda num : num**2, myNum))
checkEventLambdaList = list(map(lambda num : num%2 == 0, myNum))

def unique_list(lst):
    return set(lst)

print(unique_list([1,1,1,2,2,2,3,3,3,4,4,4]))

def multiply(numbers):
    product = 1
    for n in numbers:
        product *= n
    return product

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alpaSet = set(alphabet)
    return alpaSet <= set(str1.lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))
