name = "ArjunRamamurthy"
#print (name[1:3])
#print (name.split('R'))
#print ("Example {} {}".format(name, name.lower()))
print (f"Hello this is {name}")
print (f"This is me in reverse {name[::-1].upper().split('R')}")

myList = ['Arjun', 34, 1.0]
print (myList[0])

myDict = {'Arjun':'Ramamurthy', 'Parimala':'Shravani'}
print (myDict['Arjun'])
print (myDict['Arjun'].upper())

myDict['Nivaan'] = 'Arjun'
print (myDict)

print (type(myDict))

t = ('a','b','c','a')
print (t.count('a'))

mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(3)
print (mySet)

myFile = open('test.txt')
print (myFile.read())
print ('dummy')
myFile.seek(0)
print (myFile.readlines())
myFile.close()

with open('test.txt') as myNewFile:
   print (myNewFile.read())

with open('test.txt', 'a+') as writeFile:
   writeFile.write('\ntest6')
   writeFile.seek(0)
   print (writeFile.read())

for (key,val) in myDict.items():
    print (key,val)    

x = 0
while x < 5:
    print(f"x = {x}")
    x += 1

myList2 = list(range(0,10,2))
print (myList2)

for item in enumerate(myList2):
    print (item)

for (index,val) in enumerate(myList2):
    print ('[{}, {}]'.format(index,val))

myList3 = list(range(1,10,2))
print (myList3)

for item in zip(myList2, myList3):
    print (item)

from random import shuffle
myList = list(range(0,20))
print (myList)
shuffle(myList)
print (myList)

myString = []
for letter in 'Hello':
    myString.append(letter)
print (myString)

#List comprehensions
myList = [letter for letter in myString]
print (myList)

celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print (fahrenheit)

results = [x if x%2==0 else 'ODD' for x in range(0,10)]
print (results)

results = [x for x in range(0,10) if x%2==0]
print (results)

#nested for loop
results = [x*y for x in range(1,4) for y in range(100,400,100)]
print (results)

st = 'Print only the words that start with s in this sentence'
myWords = st.split()
for word in myWords:
    if word[0]=='s':
        print (word) 

st = 'Print every word in this sentence that has an even number of letters'
myList = [word for word in st.split() if len(word)%2==0]
print (myList)

for num in range(1,16):
    if num%15==0:
        print ('FizzBuzz')
    elif num%3==0:
        print ('Fizz')
    elif num%5==0:
        print ('Buzz')
    else:
        print (num)


def sampleFunc():
    print ("Sample Function")

sampleFunc()
