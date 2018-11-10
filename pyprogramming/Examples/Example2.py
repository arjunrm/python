def pigLatin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        pigWord = word + 'ay'
    else:
        pigWord = word[1:] + first_letter + 'ay'
    return pigWord

print (pigLatin('apple'))
print (pigLatin('word'))

def add(*args):
    print(sum(args))
    print(args)

add(1,2,3,4,5)

def fruit(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('Found fruit')
    else:
        print('No fruit')

fruit(fruit='apple',veggie='onion')

def even(*args):
    myList = list()
    for x in args:
        if x%2 == 0:
            myList.append(x)
    return myList

print(even(1,2,3,4,5,6))

def skyline(word):
    index = 0
    retStr = ""
    while index < len(word):
        if index%2 == 0:
            retStr += word[index].upper()
        else:
            retStr += word[index].lower()
        index += 1
    print(retStr)

skyline('arjun')

def old_macdonald(name):
    subStr1 = name[0:3]
    subStr2 = name[3:]
    return subStr1.capitalize() + subStr2.capitalize()

print(old_macdonald('Arjun'))

def master_yoda(text):
    words = text.split()
    return " ".join(words[::-1])

print(master_yoda("Hello how are you"))

def almost_there(n):
    return (abs(100 - n) <= 10 or abs(200-n) <= 10)

print(almost_there(94))
print(almost_there(150))
print(almost_there(209))

def has_33(nums):
    prev = 0
    for n in nums:
        if (n == 3 and prev == 3): 
            return True
        else: 
            prev = n
    return False

print("has_33 {}".format(has_33([1,3,3])))
print("has_33 {}".format(has_33([1,3,1,3])))

def paper_doll(text):
    resultStr = ""
    for c in text:
        resultStr += c * 3
    return resultStr

print("paper_doll {}".format(paper_doll("Sample")))

def blackjack(a,b,c):
    total = sum([a,b,c])
    if total <= 21:
        return total
    elif 11 in [a,b,c] and total <=21:
        return total - 10
    else:
        return 'BUST'

print("blackjack {}".format(blackjack(5,6,7)))
print("blackjack {}".format(blackjack(9,9,9)))
print("blackjack {}".format(blackjack(9,9,11)))

def summer_69(arr):
    returnVal = 0
    found6 = False
    for n in arr:
        if (n != 6 and found6 == False):
            returnVal += n
        elif (n == 6 and found6 == False):
            found6 = True
        elif (n == 9 and found6 == True):
            found6 = False
    return returnVal

print("summer_69 {}".format(summer_69([1, 3, 5])))
print("summer_69 {}".format(summer_69([4, 5, 6, 7, 8, 9])))
print("summer_69 {}".format(summer_69([2, 1, 6, 9, 11])))

def spy_game(nums):
    spy = []
    for n in nums:
        if ((n == 0 or n == 7) and (spy.__len__() < 3)):
            spy.append(n)
    return (spy == [0,0,7])

def spy_game2(nums):
    spyCode = [0,0,7,'x']
    for n in nums:
        if n == spyCode[0]:
            spyCode.pop(0)
    return len(spyCode) == 1

print("spy_game {}".format(spy_game([1,2,4,0,0,7,5])))
print("spy_game {}".format(spy_game([1,0,2,4,0,5,7])))
print("spy_game {}".format(spy_game([1,7,2,0,4,5,0])))

print("spy_game2 {}".format(spy_game2([1,2,4,0,0,7,5])))
print("spy_game2 {}".format(spy_game2([1,0,2,4,0,5,7])))
print("spy_game2 {}".format(spy_game2([1,7,2,0,4,5,0])))

def count_primes1(num):
    # check for 0 or 1
    if num < 2:
        return 0

    primes = []
    for x in range(2, num):
        count = 0
        y = 2
        while (y <= (int)(x/2)):
            if (x%y == 0):
                count += 1
                break
            y += 1
        if (count == 0):
            primes.append(x)
    print(primes)
    return primes.__len__()

def count_primes(num):
    # check for 0 or 1
    if num < 2:
        return 0

    primes = [2]
    x = 3
    while x <= num:
        #for y in range(3,x,2):
        for y in primes:
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    
    print(primes)
    return len(primes)

print("Primes {}".format(count_primes(100)))

def print_big(letter):
    patterDict = {1:'  *  \n', 2:' * * \n', 3:'*    *\n', 
    4:'*    \n', 5:'    *\n', 6:'*****\n'}

    alphabetDict = {'a':[1,2,6,3,3], 'b':[6,3,6,3,6], 'c':[6,4,4,4,6]}

    patternList = alphabetDict[letter]
    for n in patternList:
        print(patterDict[n])

print_big('a')
print_big('b')
print_big('c')
